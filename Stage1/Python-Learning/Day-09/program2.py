# capitals={
#     "France":"Paris",
#     "Germany":"Berlin",
# }

# TRAVEL_LOG={
#     "France":["Paris","Lille","Dijon"],
#     "Germany":["Berlin","Hamburg","Stuttgart"],
# }
#print(TRAVEL_LOG["France"][1])
# nested_list=["a","b",["c","d"]]
#print(nested_list[2][1])
TRAVEL_LOG={
    "France":{
        "num_of_times_visited":8,
        "cities_visited":["Paris","Lille","Dijon"],
    },
    "Germany":{
        "num_of_times_visited":5,
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
}
}
print(TRAVEL_LOG["Germany"]["cities_visited"][2] )