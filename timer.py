import HotCold.Hot_Cold_Algo as hC
from time import localtime
from os import system
import matplotlib.pyplot as plot


def test_func(number, chances, step):
    # For graph plotting of Runtime and error
    x = range(1, number + 1, step)
    fig, axis = plot.subplots()
    fig, axis2 = plot.subplots()

    error_arr, time_arr = {}, []
    count, temp = 0, chances
    for i in range(1, number + 1, step):
        tin = localtime()
        tin = tin.tm_min * 60 + tin.tm_sec
        g_obj = hC.Game(1, i+1, temp)
        algorithm_object = hC.AlgorithmSolve(g_obj, 0)
        if algorithm_object.has_won == 1:
            count += 1
            error_arr.__setitem__(str([1, g_obj.num, i + 1]), 0)
        else:
            error_arr.__setitem__(str([1, g_obj.num, i+1]), algorithm_object.error_Percentage)
        tout = localtime()
        time_arr.append((tout.tm_min * 60 + tout.tm_sec) - tin)
    line1, = axis.plot(x, time_arr, linestyle='-', label='Run-time')
    line2, = axis2.plot(list(error_arr.values()), color='red', dashes=[2, 6], label='Error')
    axis.legend()
    axis2.legend()
    plot.show()
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
    win_percentage = x[1]/num * 100
    errors = list(x[2].values())
    mean_error_percentage = mean(errors) if win_percentage > 0 else 0
    system('cls')
    print('\n\n\n\n')
    print('\nMean Run-Time for algorithm = ' + str(time_secs) + ' secs\nWin percentage = ' + str(win_percentage) + '%')
    print('Mean Error Percentage = ' + str(mean_error_percentage) + '%')
    return time_secs, win_percentage, mean_error_percentage


if __name__ == '__main__':
    return_stats(100000000, 100, 1000)
