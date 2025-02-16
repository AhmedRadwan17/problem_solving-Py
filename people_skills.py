peoples={
   "Osama":{
        "C++":"90%",
        "Python":"80%",
        "Java":"60%"
    },
   "Ahmed":{
        "C++":"40%",
        "Python":"94%",
        "Java":"50%"
   },
   "Radwan":{
        "C++":"60%",
        "Python":"88%",
        "Java":"20%"
   }
}
for name in peoples:
    print(f"People Name is:{name}")
    for skill in  peoples[name]:
      print(f"{skill} =>{peoples[name][skill]}")
    print("-"*40)