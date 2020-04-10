import HotCold.Hot_Cold_Algo as hC
from timeit import default_timer
import matplotlib.pyplot as plt
from os import system


def test_func(number, chances, step):
    # For graph plotting of Runtime and error
    x = range(1, number + 1, step)
    fig, axis = plt.subplots()
    fig, axis2 = plt.subplots()

    error_arr, time_arr = {}, []
    count, temp = 0, chances
    for i in range(1, number + 1, step):
        tin = default_timer()
        g_obj = hC.Game(1, i+1, temp)
        algorithm_object = hC.AlgorithmSolve(g_obj, 0)
        if algorithm_object.has_won == 1:
            count += 1
            error_arr.__setitem__(str([1, g_obj.num, i + 1]), 0)
        else:
            error_arr.__setitem__(str([1, g_obj.num, i+1]), algorithm_object.error_Percentage)
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


def mean(lis):
    s = 0
    for i in lis:
        s += i
    s /= len(lis)
    return s


def return_stats(num, tries, step):
    x = test_func(num, tries, step)
    time_secs = mean(x[0])
    win_percentage = x[1]/(num/step) * 100
    errors = list(x[2].values())
    mean_error_percentage = mean(errors) if win_percentage > 0 else 0
    system('cls')

    string = 'For %d tries:\n' % tries
    string += '\nMean Run-Time for algorithm = ' + str(time_secs) + ' secs\nWin percentage = ' + str(win_percentage)
    string += '%\nMean Error Percentage = ' + str(mean_error_percentage) + '%\n\n\n'

    print('\n\n\n' + string)
    f.write(string)

    return time_secs, win_percentage, mean_error_percentage


if __name__ == '__main__':
    f = open("statistics.txt", 'w')

    # Syntax: return_stats(Order_of_range, Number_of_tries, Step_size)
    return_stats(100000000, 10, 10000)
    return_stats(100000000, 100, 10000)
    return_stats(100000000, 1000, 10000)

    f.close()

