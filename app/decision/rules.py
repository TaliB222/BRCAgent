def should_respond(classification: dict) -> bool:
    # Safety check - אם אין מידע בסיסי
    if not classification:
        return False

    # לא רלוונטי לתחום הרפואי
    if not classification.get("relevant", False):
        return False

    # שליפת שדות עם ברירת מחדל
    intent = classification.get("intent", "")
    sensitivity = classification.get("sensitivity_level", "")
    should_respond_flag = classification.get("should_respond", False)

    # 🚫 מצבים שבהם לא נגיב (בטיחות)
    if sensitivity == "high":
        # אם אין שאלה ברורה - לא מגיבים
        if intent in ["sharing", "emotional_support"]:
            return False

    if sensitivity == "medium":
        # עדיין זהיר עם תוכן רגשי
        if intent == "emotional_support":
            return False

    # אל תסמכי רק על המודל - אחרת נחסמות שאלות רפואיות לגיטימיות
    if should_respond_flag is False and intent != "question":
        return False

    # ✅ רק מקרים לגיטימיים
    if intent in ["question", "general_discussion"]:
        return True

    return False