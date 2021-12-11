from classes import person

N = 1000      # number of people
ROI = 2       # Radius Of Infection
RECOVERY = 5  # days needed to recover

# populate array of people
people = [person(0, 0) for _ in range(N)]
people[0].Infected = True

while True:
    #plot_x = []
    #plot_y = []
    for i in range(N):
        people[i].is_infected(people, ROI)
        if people[i].Infected:
            people[i].daysInfected += 1
        people[i].is_recovered(RECOVERY)
        people[i].change_pos()
        #plot_x.append(people[i].x)
        #plot_y.append(people[i].y)
        #plt.scatter(people[i].x, people[i].y)
    break
#plt.show()