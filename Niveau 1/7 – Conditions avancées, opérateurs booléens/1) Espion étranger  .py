Start_date=int(input())
end_date=int(input())
nb_entries=int(input())
nb_people=0
for i in range(nb_entries):
    if Start_date<=int(input())<=end_date:
        nb_people=nb_people+1
print(nb_people)