"""Behavioral regression tests for approved OOP teaching examples."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "technical-interview-preparation"


def load_example(chapter, name):
    path = ROOT / chapter / "examples" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class InterviewOOPTests(unittest.TestCase):
    def test_independent_instances_and_validation(self):
        m = load_example("05-classes-and-objects", "reading_session")
        first, second = m.ReadingSession("Python"), m.ReadingSession("SQL")
        first.read(4)
        self.assertEqual(first.pages, 4)
        self.assertEqual(second.pages, 0)
        with self.assertRaises(ValueError):
            first.read(-1)
        self.assertEqual(first.pages, 4)
        first.read(0)
        self.assertEqual(first.pages, 4)
        for value in (True, 1.5, "2"):
            with self.subTest(value=value), self.assertRaises(TypeError):
                first.read(value)
        self.assertEqual(first.pages, 4)

    def test_method_kinds_and_shared_vs_instance_state(self):
        m = load_example("06-attributes-methods-and-object-behavior", "study_group")
        group = m.StudyGroup.from_label("  Python  ")
        other = m.StudyGroup("SQL")
        group.add("Ada")
        self.assertEqual(group.label, "Python")
        self.assertEqual(len(group), 1)
        self.assertEqual(len(other), 0)
        self.assertEqual(m.StudyGroup.category, "study")
        self.assertFalse(m.StudyGroup.valid_label(" "))
        self.assertEqual(str(group), "Python: 1")
        self.assertEqual(repr(group), "StudyGroup(label='Python', members=['Ada'])")
        self.assertEqual(other.category, m.StudyGroup.category)
        self.assertTrue(m.StudyGroup.valid_label("Python"))
        self.assertFalse(m.StudyGroup.valid_label(None))

    def test_alternative_constructor_preserves_subclass_and_validation(self):
        m = load_example("06-attributes-methods-and-object-behavior", "study_group")

        class AdvancedGroup(m.StudyGroup):
            pass

        group = AdvancedGroup.from_label("  Python  ")
        self.assertIs(type(group), AdvancedGroup)
        self.assertEqual(group.label, "Python")
        for constructor in (m.StudyGroup, m.StudyGroup.from_label):
            for invalid in ("", " ", None, 42):
                with self.subTest(constructor=constructor, invalid=invalid):
                    with self.assertRaises(ValueError):
                        constructor(invalid)

    def test_polymorphism_and_composition(self):
        m = load_example("07-inheritance-polymorphism-and-composition", "notifications")
        self.assertTrue(issubclass(m.TextChannel, m.Channel))
        self.assertTrue(issubclass(m.EmailChannel, m.Channel))
        with self.assertRaises(NotImplementedError):
            m.Channel().send("Ready")
        self.assertEqual(m.Notifier(m.TextChannel()).notify("Ready"), "text: Ready")
        self.assertEqual(m.Notifier(m.EmailChannel()).notify("Ready"), "email: Ready")
        class FakeChannel:
            def send(self, message):
                return message.upper()
        self.assertEqual(m.Notifier(FakeChannel()).notify("Ready"), "READY")

    def test_invariant_and_abstraction(self):
        m = load_example("08-encapsulation-abstraction-and-solid", "stock")
        stock = m.Stock(3)
        stock.remove(2)
        self.assertEqual(stock.quantity, 1)
        with self.assertRaises(ValueError):
            stock.remove(2)
        self.assertEqual(stock.quantity, 1)
        with self.assertRaises(ValueError):
            stock.remove(-1)
        with self.assertRaises(TypeError):
            m.StockReader()
        self.assertEqual(m.remaining(m.InMemoryStockReader(stock)), 1)
        self.assertEqual(stock.quantity, 1)
        with self.assertRaises(AttributeError):
            stock.quantity = 99
        for value in (True, 1.5, "2"):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    m.Stock(value)
                with self.assertRaises(TypeError):
                    stock.remove(value)
        with self.assertRaises(ValueError):
            m.Stock(-1)
        self.assertEqual(stock.quantity, 1)
        stock.remove(0)
        self.assertEqual(stock.quantity, 1)
        stock.remove(1)
        self.assertEqual(stock.quantity, 0)
        self.assertEqual(m.remaining(m.InMemoryStockReader(stock)), 0)

        class FakeReader(m.StockReader):
            def available(self):
                return 7

        self.assertEqual(m.remaining(FakeReader()), 7)


if __name__ == "__main__":
    unittest.main()
