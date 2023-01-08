# In this porject, this script is used for handling data related to growthrates of different bacteria at different temperatures
import os
import numpy as np
import matplotlib.pyplot as plt


# Data load function
def dataLoad(filename):
    """
    The function read the data in the data file 'filename'. Each line in the data file consists of the following fields:
    'Temperature','Growth rate','Bacteria'
    :param filename: A string containing the filename of a data file
    :return: data: An N*3 matrix
    """
    print('Loading')
    data = np.loadtxt(filename)
    Temperature = data[:, 0]
    Growth_rate = data[:, 1]
    Bacteria = data[:, 2]
    tem = np.zeros(len(Temperature))
    rate = np.zeros(len(Temperature))
    bac = np.zeros(len(Temperature))
    i = 0
    while True:
        if (10 < Temperature[i] < 60) and (Growth_rate[i] > 0) and (
                Bacteria[i] == 1 or Bacteria[i] == 2 or Bacteria[i] == 3 or Bacteria[i] == 4):
            tem[i] = Temperature[i]
            rate[i] = Growth_rate[i]
            bac[i] = Bacteria[i]
            i = i + 1
        elif (Temperature[i] < 10) or (Temperature[i] > 60):
            print('The %d line contains the error Temperature information, please check' % i)
            i = i + 1
        elif Growth_rate[i] <= 0:
            print('The %d line contains the error Growth rate information, please check' % i)
            i = i + 1
        elif (Bacteria[i] != 1) or (Bacteria[i] != 2) or (Bacteria[i] != 3) or (Bacteria[i] != 4):
            print('The %d line contains the error Bacteria index information, please check' % i)
            i = i + 1
        if i == len(Temperature):
            # get the modified data
            data = np.array([tem, rate, bac])
            return data.T
            print(data)
    return data


def dataStatistics(data, statistic):
    """
    This function calculates one of several possible statistics based on the data
    :param data: An N*3 matrix with columns Temperature, Growth rate, and Bacteria
    :param statistic: A string specifying the statistic that should be calculated
    :return: results: A scalar containing the calculated statistic
    """
    tem = data[:, 0]
    rate = data[:, 1]
    bac = data[:, 2]
    if statistic == 'Mean Temperature':
        mean_tem = np.mean(tem)
        result = mean_tem
    elif statistic == 'Mean Growth rate':
        mean_rate = np.mean(rate)
        result = mean_rate
    elif statistic == 'Std Temperature':
        std_tem = np.std(tem)
        result = std_tem
    elif statistic == 'Std Growth rate':
        std_rate = np.std(rate)
        result = std_rate
    elif statistic == 'Rows':
        rows = len(tem)
        result = rows
    elif statistic == 'Mean Cold Growth rate':
        coldRate = rate[tem < 20]
        mean_coldRate = np.mean(coldRate)
        result = mean_coldRate
    elif statistic == 'Mean Hot Growth rate':
        hotRate = rate[tem > 50]
        mean_hotRate = np.mean(hotRate)
        result = mean_hotRate

    return result


def dataPlot(data):
    """
    This function will display two plots:
    1. The bar plot of the number of each of the different types of Bacteria in the data
    2. The Growth rate by temperature
    :param data: An N*3 matrix with columns Temperature, Growth rate and Bacteria
    :return: None
    """
    tem = data[:, 0]
    rate = data[:, 1]
    bac = data[:, 2]
    # count the number of different kinds bacteria
    num = np.zeros(4)
    for i in range(4):
        num[i] = len(bac[bac == i + 1])

    # plot the number of each of the types
    plt.figure()
    label_list = np.array(['Salmonella enterica', 'Bacillus cereus', 'Listeria', 'Brochothrix thermosphacta'])
    colors = ['red', 'green', 'blue', 'cyan']
    plt.bar(range(len(num)), num, color=colors, tick_label=label_list)
    plt.xlabel('The type of Bacteria', fontsize=15)
    plt.ylabel('The number of each Bacteria', fontsize=15)
    plt.title('Number of bacteria', fontsize=15)
    plt.show()
    # plot the growth rate by temperature
    plt.figure()
    for i in range(4):
        plt.plot(tem[bac == i + 1], rate[bac == i + 1], 'kx')
        plt.plot(tem[bac == i + 1], rate[bac == i + 1], ':', label=label_list[i])

    plt.xticks(range(10, 60, 2))
    plt.legend()
    plt.title('Growth rate by temperature', fontsize=15)
    plt.xlabel('Temperature', fontsize=15)
    plt.ylabel('Growth rate', fontsize=15)
    plt.show()


def filterPrint(filter_index):
    print('' * 79)
    if np.size(filter_index) == 2:
        print(' ' * 21 + 'The Growth rate is chosen between %s and %s' % (filter_index[0], filter_index[1]))
    else:
        if filter_index == 0:
            print(' ' * 25 + 'No filter implementation')
        elif filter_index == 'bac_1':
            print(' ' * 21 + 'Salmonella enterica bacteria is chosen')
        elif filter_index == 'bac_2':
            print(' ' * 23 + 'Bacillus cereus bacteria is chosen')
        elif filter_index == 'bac_3':
            print(' ' * 25 + 'Listeria bacteria is chosen')
        elif filter_index == 'bac_4':
            print(' ' * 21 + 'Brochothrix thermosphacta bacteria is chosen')


def filterData(data_origin, number):
    """
    This function is used to help user filter data and clear filter
    :param data_origin: The origin data
    :param number: 1-5
    :return: filter_index: the number of filtered bac, data_filter: the filtered data
    """
    tem = data_origin[:, 0]
    rate = data_origin[:, 1]
    bac = data_origin[:, 2]
    if np.size(number) == 1:
        if number == '1':
            tem = tem[bac == 1]
            rate = rate[bac == 1]
            bac = bac[bac == 1]
            filter_index = 'bac_1'
        elif number == '2':
            tem = tem[bac == 2]
            rate = rate[bac == 2]
            bac = bac[bac == 2]
            filter_index = 'bac_2'
        elif number == '3':
            tem = tem[bac == 3]
            rate = rate[bac == 3]
            bac = bac[bac == 3]
            filter_index = 'bac_3'
        elif number == '4':
            tem = tem[bac == 4]
            rate = rate[bac == 4]
            bac = bac[bac == 4]
            filter_index = 'bac_4'
        elif number == '0':
            tem = data_origin[:, 0]
            rate = data_origin[:, 1]
            bac = data_origin[:, 2]
            filter_index = 0
        data_filter = np.array([tem, rate, bac]).T
    elif np.size(number) == 2:
        low_num = float(number[0])
        high_num = float(number[1])
        tem = tem[rate >= low_num]
        rate1 = rate[rate >= low_num]
        bac = bac[rate >= low_num]
        tem = tem[rate1 <= high_num]
        rate2 = rate1[rate1 <= high_num]
        bac = bac[rate1 <= high_num]
        data_filter = np.array([tem,rate2,bac]).T
        filter_index = number
    os.system('cls')
    return data_filter, filter_index


if __name__ == '__main__':
    """
    The main function of the script
    # Create interation pages for users
    # Users select function based on prompts
    # Recognizes the user's input and thus execute the corresponding function
    """
    data = []
    # filter_index is used for helping determine if the filter is used
    filter_index = 0
    while True:
        print('-' * 20 + 'Welcome to Bacteria Data Analysis' + '-' * 21)
        print('-' * 35 + 'Menu' + '-' * 35)
        print('-' * 30 + '[1]: Load data' + '-' * 30)
        print('-' * 30 + '[2]: Filter data' + '-' * 28)
        print('-' * 30 + '[3]: Display statistics' + '-' * 21)
        print('-' * 30 + '[4]: Generate plots' + '-' * 25)
        print('-' * 30 + '[5]: Quit' + '-' * 35)
        filterPrint(filter_index)
        number = input('Please input a number:')

        if number == '1':
            os.system('cls')
            filename = input('Please input the filename of a data file\n')
            data = dataLoad(filename)
            print('Data has been loaded successfully')
            os.system('pause')
            os.system('cls')
            data_origin = data.copy()

        elif number == '2':
            os.system('cls')
            if len(data) == 0:
                print('There is no data loading, please load data first')
                os.system('pause')
            else:

                tem = data[:, 0]
                rate = data[:, 1]
                bac = data[:, 2]
                print('-' * 30 + 'Filter data' + '-' * 50)
                print('-' * 30 + '[1]: Filter the types of Bacteria' + '-' * 28)
                print('-' * 30 + '[2]: Filter the range for Growth rate' + '-' * 24)
                print('-' * 30 + '[3]: Return to previous page' + '-' * 33)
                print('-' * 30 + '[0]: Clear the filter' + '-' * 33)
                filterPrint(filter_index)
                number = input('Please input a number:')
                os.system('cls')
                if number == '1':
                    os.system('cls')
                    print('-' * 30 + 'Filter the types of Bacteria' + '-' * 28)
                    print('-' * 30 + '[1]: Salmonella enterica' + '-' * 28)
                    print('-' * 30 + '[2]: Bacillus cereus' + '-' * 24)
                    print('-' * 30 + '[3]: Listeria' + '-' * 24)
                    print('-' * 30 + '[4]: Brochothrix thermosphacta' + '-' * 33)
                    filterPrint(filter_index)
                    num = input('Please input a number:')
                    data_filter, filter_index = filterData(data_origin, num)
                elif number == '2':
                    # Filter the range of Growth rate
                    os.system('cls')
                    print('-' * 30 + 'Filter the range for Growth rate' + '-' * 28)
                    low_num = input('Please input the low range of the Growth rate [0-1]:')
                    high_num = input('Please input the high range of the Growth rate [0-1]:')
                    print('Now the range of Growth rate is %s < Growth rate <%s' % (low_num, high_num))
                    filter_index = np.array([low_num, high_num])
                    num = filter_index
                    data_filter, _ = filterData(data_origin, num)
                elif number == '3':
                    continue
                elif number == '0':
                    data_filter, filter_index = filterData(data_origin, number)
                data = data_filter

        elif number == '3':
            os.system('cls')
            # This number is used for determining if there is a filter using
            if len(data) == 0:
                print('There is no data loading, please load data first')
                os.system('pause')
            else:
                print('-' * 30 + 'Display statistics' + '-' * 31)
                print('-' * 30 + '[1]: Mean Temperature' + '-' * 28)
                print('-' * 30 + '[2]: Mean Growth rate' + '-' * 28)
                print('-' * 30 + '[3]: Std Temperature' + '-' * 29)
                print('-' * 30 + '[4]: Std Growth rate' + '-' * 29)
                print('-' * 30 + '[5]: Total number of rows' + '-' * 24)
                print('-' * 30 + '[6]: Mean Cold Growth rate' + '-' * 23)
                print('-' * 30 + '[7]: Mean Hot Growth rate' + '-' * 24)
                print('-' * 30 + '[8]: Return to previous page' + '-' * 21)
                filterPrint(filter_index)
                number = input('Please input a number:')
                if number == '1':
                    statistic = 'Mean Temperature'
                elif number == '2':
                    statistic = 'Mean Growth rate'
                elif number == '3':
                    statistic = 'Std Temperature'
                elif number == '4':
                    statistic = 'Std Growth rate'
                elif number == '5':
                    statistic = 'Rows'
                elif number == '6':
                    statistic = 'Mean Cold Growth rate'
                elif number == '7':
                    statistic = 'Mean Hot Growth rate'
                elif number == '8':
                    os.system('cls')
                    continue
                result = dataStatistics(data, statistic)
                print('The %s of data is %f' % (statistic, result))
                os.system('pause')
                os.system('cls')

        elif number == '4':
            os.system('cls')
            if len(data) == 0:
                print('There is no data loading, please load data first')
                os.system('pause')
            else:
                dataPlot(data)

        elif number == '5':
            os.system('cls')
            print('Thanks for using the Bacteria Data Analysis')
            break
        else:
            os.system('cls')
            print('Invalid command, please input number from 1 to 5')
            os.system('pause')
            os.system('cls')

    # filename = 'test.txt'
    # data = dataLoad(filename)
    # result = dataStatistics(data,'Mean Hot Growth rate')
    # dataPlot(data)
