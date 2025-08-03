def match_intent(query, data):
    query = query.lower()
    
    if "রুটিন" in query:
        return "routine", get_routine(data)
    elif "স্যার" in query or "রুম" in query:
        return "teacher", get_teacher_room(data)
    elif "ইভেন্ট" in query or "ঘোষণা" in query:
        return "event", data.get("events", "কোনো ইভেন্ট তথ্য পাওয়া যায়নি।")
    else:
        return "unknown", "আমি নিশ্চিত না আপনি কী জানতে চাচ্ছেন। আবার বলুন।"

def get_routine(data):
    routine = data.get("routine", {})
    msg = "📅 ক্লাস রুটিন:\n"
    for day, classes in routine.items():
        msg += f"\n🗓️ {day}:\n"
        for c in classes:
            # Optional: Validate keys exist before accessing
            time = c.get('time', 'সময় জানা নেই')
            course = c.get('course', 'কোর্স জানা নেই')
            room = c.get('room', 'রুম জানা নেই')
            msg += f"  🕒 {time}: {course} ({room})\n"
    return msg.strip()

def get_teacher_room(data):
    teachers = data.get("teachers", {})
    msg = "👨‍🏫 স্যারদের রুম নম্বর:\n"
    for name, info in teachers.items():
        room = info.get('room', 'রুম জানা নেই')
        msg += f"  {name}: Room {room}\n"
    return msg.strip()
