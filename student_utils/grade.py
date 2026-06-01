def get_grade(avg): 
    if avg>=90:
        return "A"
    elif avg>=75:
        return "B"
    elif avg>=60:
        return "C"
    elif avg>=50:
        return "D"
    else:
        return "F"