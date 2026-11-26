"""Behavioral tests for the Phase 12 Python internals examples."""
import importlib.util
from pathlib import Path
from threading import Lock
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1] / "technical-interview-preparation"


def load_example(chapter, name):
    path = ROOT / chapter / "examples" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class InternalsTests(unittest.TestCase):
    def test_copy_preserves_original_and_internal_aliases(self):
        m = load_example("09-object-identity-references-and-copying", "copy_plan")
        shared = ["draft"]
        original = {"first": shared, "second": shared}
        result = m.clone_plan(original)
        self.assertIsNot(result, original)
        self.assertIsNot(result["first"], shared)
        self.assertIs(result["first"], result["second"])
        result["first"].append("done")
        self.assertEqual(shared, ["draft"])
        self.assertEqual(result["second"], ["draft", "done"])

    def test_bounded_cache_evicts_and_does_not_retain_removed_key(self):
        m = load_example("10-python-memory-management", "bounded_cache")
        cache = m.BoundedCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("a", 3)
        cache.put("c", 4)
        self.assertEqual(cache.snapshot(), {"a": 3, "c": 4})
        cache.clear()
        self.assertEqual(cache.snapshot(), {})
        for invalid in (0, -1, True, 1.5):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                m.BoundedCache(invalid)

    def test_generator_is_lazy_and_exhausts(self):
        m = load_example("11-iterators-generators-and-comprehensions", "eligible_rows")
        seen = []
        def source():
            for row in (0, 3, 1, 4):
                seen.append(row)
                yield row
        stream = m.eligible_rows(source(), 3)
        self.assertEqual(seen, [])
        self.assertIs(iter(stream), stream)
        self.assertEqual(next(stream), 3)
        self.assertEqual(seen, [0, 3])
        self.assertEqual(list(stream), [4])
        self.assertEqual(list(stream), [])
        self.assertEqual(list(m.eligible_rows([], 3)), [])

    def test_closures_are_independent_and_wrapper_preserves_contract(self):
        m = load_example("12-closures-and-decorators", "call_counter")
        first, second = m.make_counter(), m.make_counter()
        self.assertEqual([first(), first(), second()], [1, 2, 1])
        calls = []
        @m.record_calls(calls)
        def divide(numerator, denominator):
            return numerator / denominator
        self.assertEqual(divide(6, denominator=2), 3)
        self.assertEqual(divide.__name__, "divide")
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)
        self.assertEqual(calls, ["divide", "divide"])

    def test_context_cleanup_and_exception_propagation(self):
        m = load_example("13-context-managers", "managed_session")
        events = []
        with m.managed_session(events) as session:
            self.assertIs(session, events)
            events.append("work")
        self.assertEqual(events, ["open", "work", "close"])
        events.clear()
        with self.assertRaisesRegex(RuntimeError, "failure"):
            with m.managed_session(events):
                raise RuntimeError("failure")
        self.assertEqual(events, ["open", "close"])

    def test_lock_protects_counter_and_workers_finish(self):
        m = load_example("14-concurrency-parallelism-and-the-gil", "safe_counter")
        self.assertEqual(m.count_updates(4, 250), 1000)
        self.assertEqual(m.count_updates(3, 0), 0)
        for workers, updates in ((0, 1), (1, -1), (True, 1)):
            with self.subTest(workers=workers, updates=updates):
                with self.assertRaises(ValueError):
                    m.count_updates(workers, updates)


    def test_every_counter_update_enters_shared_lock(self):
        m = load_example("14-concurrency-parallelism-and-the-gil", "safe_counter")

        class RecordingLock:
            def __init__(self):
                self.lock = Lock()
                self.entries = 0
                self.exits = 0

            def __enter__(self):
                self.lock.acquire()
                self.entries += 1
                return self

            def __exit__(self, exc_type, exc_value, traceback):
                self.exits += 1
                self.lock.release()
                return False

        workers, updates = 4, 25
        recording = RecordingLock()
        # Count actual critical-section entries, independent of scheduling.
        with patch.object(m, "Lock", return_value=recording) as factory:
            self.assertEqual(m.count_updates(workers, updates), workers * updates)
        factory.assert_called_once_with()
        self.assertEqual(recording.entries, workers * updates)
        self.assertEqual(recording.exits, workers * updates)


if __name__ == "__main__":
    unittest.main()
