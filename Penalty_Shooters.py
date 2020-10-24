def game():

    print("Please input the number of test cases you would like to check:")
    # Takes the number of test games to be run
    T = int(input())

    print("Now please input the energies of Lohia, Gosu and Prince, respectively. Your goals scored by Lohia and Gosu will follow:")

    for x in range(T):
            # Allows us to input and apply method to all iterables in a | no. of tests \n x_energy y_energy z_energy | format. T = number of tests, x is Lohia energy, y is Gosu energy and z is Goalkeeper energy
            x, y, z = list(map(int, input().split(" ")))
            Goal_Lohia, Goal_Gosu = 0, 0

            # Session ends when goalkeepers energy decrements to 1
            while z > 1:
                # Goalkeepers energy in this case is a factor of both strikers' energy, but Lohia is preferred due to being younger.
                if x % z == 0 and y%z == 0:
                    x = x - 1
                    Goal_Lohia = Goal_Lohia + 1
                # In this case, the goalkeepers energy is only a factor of Lohia's. Note Lohia goes first as the problem states.
                elif x % z == 0:
                    x = x - 1
                    Goal_Lohia = Goal_Lohia + 1
                # And in this case, it is only a factor of Gosu's
                elif y % z == 0:
                    y = y - 1
                    Goal_Gosu = Goal_Gosu + 1
                # If goalkeepers energy is a factor of neither Gosu nor Lohia, the goalkeeper will save (no goal scored) and will lose energy.
                else:
                    z = z - 1
            print(Goal_Lohia, Goal_Gosu)



game()
