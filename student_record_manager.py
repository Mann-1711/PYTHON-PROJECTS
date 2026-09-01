#THIS IS A SMALL PROJECT MADE BY ME TO PRACTICE DICTIONARIES AND SETS.
recordes={
    "name":"manraj singh",
    "course":"BCA AIML",
    "subjects":{"python","english","maths","data engineering"},
    "marks":{
        "python":78,
        "english":84,
        "maths":67,
        "data engineering":77
    }
}
recordes["marks"].update({"python":82})
recordes["subjects"].update({"C"})
recordes["marks"].update({"C":69})
recordes.pop("course")
print(recordes)
