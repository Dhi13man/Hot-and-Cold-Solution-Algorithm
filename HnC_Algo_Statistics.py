import Hot_Cold_Algo as hC
from timeit import default_timer
import matplotlib.pyplot as plt
from os import system


# Finds runtime, whether there was a win and Error across multiple runs
def test_func(game_range_order, chances, step):
    # For graph plotting of Runtime and error
    x = range(1, game_range_order + 1, step)
    fig, axis = plt.subplots()
    fig, axis2 = plt.subplots()

    error_arr, time_arr = {}, []
    count, temp = 0, chances
    for i in range(1, game_range_order + 1, step):
        tin = default_timer()
        g_obj = hC.Game(1, i + 1, temp)
        algorithm_object = hC.AlgorithmSolve(g_obj, 0)
        if algorithm_object.has_won == 1:
            count += 1
            error_arr.__setitem__(str([1, g_obj.target_number, i + 1]), 0)
        else:
            error_arr.__setitem__(str([1, g_obj.target_number, i + 1]), algorithm_object.error_Percentage)
        time_arr.append(default_timer() - tin)

    # Plotting of the statistical data
    axis.plot(x, time_arr, label='Run-time')
    axis.legend()
    axis.grid()
    axis.set_xlabel('Range Upper Limit')
    axis.set_ylabel('Run-Time')
    axis2.plot(x, list(error_arr.values()), color='red', dashes=[2, 6], label='Error')
    axis2.legend()
    axis2.grid()
    axis2.set_xlabel('Range Upper Limit')
    axis2.set_ylabel('Percentage Error (if not correct value)')

    plt.show()
    return time_arr, count, error_arr


# Helper function to find mean of any list
def mean(lis):
    s = 0
    for i in lis:
        s += i
    s /= len(lis)
    return s


# Calls Test Function to return statistical data to main
def return_stats(num, tries, step):
    file = open("statistics.txt", 'w')
    x = test_func(num, tries, step)
    time_secs = mean(x[0])
    win_percentage = x[1] / (num / step) * 100
    errors = list(x[2].values())
    mean_error_percentage = mean(errors) if win_percentage > 0 else 0
    system('cls')

    string = 'For %d tries:\n' % tries
    string += '\nMean Run-Time for algorithm = ' + str(time_secs) + ' secs\nWin percentage = ' + str(win_percentage)
    string += '%\nMean Error Percentage = ' + str(mean_error_percentage) + '%\n\n\n'

    print('\n\n\n' + string)
    file.write(string)
    file.close()

    return time_secs, win_percentage, mean_error_percentage


# Performs multiple games and algorithm runs, to find average minimum chances required to solve any game
def find_chances_threshold(game_range_order, step):
    file = open("statistics.txt", 'a')
    no_of_guesses = []
    for i in range(1, game_range_order + 1, step):
        g_obj = hC.Game(1, i + 1, game_range_order)
        algorithm_object = hC.AlgorithmSolve(g_obj, 0);
        no_of_guesses.append(len(algorithm_object.guess_list))
    file.write("\n***************************************************\n" +
               "Average minimum guesses needed to win = " + str(mean(no_of_guesses)) + "\n\n")
    file.close()


if __name__ == '__main__':
    # Syntax: return_stats(Order_of_range, Number_of_tries, Step_size)
    return_stats(100000000, 10, 10000)
    return_stats(100000000, 100, 10000)
    return_stats(100000000, 1000, 10000)
    find_chances_threshold(1000000000, 10000)
