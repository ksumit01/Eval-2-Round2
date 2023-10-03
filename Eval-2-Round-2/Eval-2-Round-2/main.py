def  allocate_projects (List1, List2):
  assignment = []
  for i in List1:
    for j in List2:
     if all(skill in List1["skills"] for skill in j["required_skills"]):
      i["current_project"] = j["name"]
      assignment.append({"i":List1["name"],"j":j["name"]})
      List2.remove(j)
      break
  return assignment
