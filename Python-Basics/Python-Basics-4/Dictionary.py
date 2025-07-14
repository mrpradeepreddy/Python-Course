# key : Value pairs,unordered,no duplicates,mutable
dict={
    "name":"ram",
    "subject":["maths","physics"],
    "courses":("ai","genai"),
    "cgpa":9.6,
    "marks":[98,97,95]
}

# null_dict={}
# print(dict)
# dict["name"]="ra"   #overwrite
# dict["surname"]="pS"
# print(dict)
# print(dict.keys())
# print(list(dict.keys()))
# print(len(list(dict.keys())))
# print(dict.values())
# print(dict.items())
print(dict.get("name"))
dict.update({"name":"rams"})
print(dict)


