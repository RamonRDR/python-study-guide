study_queue = ["strings", "numbers"]

study_queue.append("lists")
study_queue.insert(1, "variables")
study_queue.remove("numbers")
completed_topic = study_queue.pop(0)

print("Completed:", completed_topic)
print("Queue:", study_queue)
