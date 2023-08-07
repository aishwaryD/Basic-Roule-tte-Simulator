"""
Just an example
"""

import numpy as np
import matplotlib.pyplot as plt


def author():
    return "aishwaryD"

def get_spin_result(win_prob):
    result = False  		  	   		  		 			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		  		 			  		 			     			  	 
        result = True
    return result  		  	   		  		 			  		 			     			  	 

def test_code():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Method to test the code  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    win_prob = 0.474
    np.random.seed(gtid())

    plot_chart(win_prob, plot_type="expt1_fig1", bankroll=float('inf'))
    plot_chart(win_prob, plot_type="expt1_fig2", bankroll=float('inf'))
    plot_chart(win_prob, plot_type="expt1_fig3", bankroll=float('inf'))
    plot_chart(win_prob, plot_type="expt2_fig1", bankroll=256)
    plot_chart(win_prob, plot_type="expt2_fig2", bankroll=256)

"""
Implementations     
"""

def american_roulette_simulator(win_prob, limited_bankroll, bankroll_amount):
    winnings_array = np.full(1001, 0)
    episode_winnings = 0
    winnings_array[0] = 0
    counter = 1

    while episode_winnings < 80:
        won = False
        bet_amount = 1
        while not won:
            won = get_spin_result(win_prob)
            if won:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2

                if limited_bankroll:
                    if episode_winnings == -bankroll_amount:
                        winnings_array[counter:] = episode_winnings
                        return winnings_array

                    if episode_winnings - bet_amount < -bankroll_amount:
                        bet_amount = bankroll_amount + episode_winnings

            if counter >= 1001:
                return winnings_array

            winnings_array[counter] = episode_winnings
            counter += 1

    if episode_winnings == 80:
        winnings_array[counter:] = episode_winnings

    return winnings_array


def plot_chart(win_prob, plot_type, bankroll):
    plt.axis([0, 300, -256, 100])
    data_storage_array = np.empty((1000, 1001))

    if plot_type == "expt1_fig1":

        plt.title("10 Episodes with infinite bankroll | Experiment 1, Figure 1")
        plt.xlabel("Number of Spins")
        plt.ylabel("Winnings in USD")

        for episode in range(1, 11):
            result = american_roulette_simulator(win_prob, limited_bankroll=False, bankroll_amount=bankroll)
            plt.plot(result, label="Episode {}" .format(str(episode)))

        plt.legend()
        plt.savefig("experiment1_figure1.png")
        plt.clf()

    elif plot_type == "expt1_fig2":
        plt.title("1000 Episodes with infinite bankroll | Experiment 1, Figure 2")
        plt.xlabel("Number of Spins")
        plt.ylabel("Mean Value of Winnings in USD")

        result_array = get_data(win_prob, plot_type="expt1_fig2", bankroll=bankroll)
        data_storage_array = result_array
        np_mean_array = np.mean(data_storage_array, axis=0)
        np_standard_deviation = np.std(data_storage_array, axis=0)
        above_mean_array = np_mean_array + np_standard_deviation
        below_mean_array = np_mean_array - np_standard_deviation

        plt.plot(np_mean_array, label="Mean")
        plt.plot(above_mean_array, label="Mean+Std")
        plt.plot(below_mean_array, label="Mean-Std")

        plt.legend()
        plt.savefig("experiment1_figure2.png")
        plt.clf()

    elif plot_type == "expt1_fig3":
        plt.title("1000 Episodes with infinite bankroll | Experiment 1, Figure 3")
        plt.xlabel("Number of Spins")
        plt.ylabel("Median Value of Winnings in USD")

        np_median_array = np.median(data_storage_array, axis=0)
        np_standard_deviation = np.std(data_storage_array, axis=0)
        above_median_array = np_median_array + np_standard_deviation
        below_median_array = np_median_array - np_standard_deviation

        plt.plot(np_median_array, label="Median")
        plt.plot(above_median_array, label="Median+Std")
        plt.plot(below_median_array, label="Median-Std")

        plt.legend()
        plt.savefig("experiment1_figure3.png")
        plt.clf()

    elif plot_type == "expt2_fig1":

        plt.title("1000 Episodes with $ {} bankroll | Experiment 2, Figure 1".format(str(bankroll)))
        plt.xlabel("Number of Spins")
        plt.ylabel("Mean Value of Winnings in USD")

        result_array = get_data(win_prob, plot_type="expt2_fig1", bankroll=bankroll)
        data_storage_array = result_array

        np_mean_array = np.mean(data_storage_array, axis=0)
        np_standard_deviation = np.std(data_storage_array, axis=0)
        above_mean_array = np_mean_array + np_standard_deviation
        below_mean_array = np_mean_array - np_standard_deviation

        plt.plot(np_mean_array, label="Mean")
        plt.plot(above_mean_array, label="Mean+Std")
        plt.plot(below_mean_array, label="Mean-Std")

        plt.legend()
        plt.savefig("experiment2_figure1.png")
        plt.clf()

    elif plot_type == "expt2_fig2":

        plt.title("1000 Episodes with $ {} bankroll | Experiment 2, Figure 2".format(str(bankroll)))
        plt.xlabel("Number of Spins")
        plt.ylabel("Median Value of Winnings in USD")

        np_median_array = np.median(data_storage_array, axis=0)
        np_standard_deviation = np.std(data_storage_array, axis=0)
        above_median_array = np_median_array + np_standard_deviation
        below_median_array = np_median_array - np_standard_deviation

        plt.plot(np_median_array, label="Median")
        plt.plot(above_median_array, label="Median+Std")
        plt.plot(below_median_array, label="Median-Std")

        plt.legend()
        plt.savefig("experiment2_figure2.png")
        plt.clf()

    else:
        print("Please enter the correct plot type")


def get_data(win_prob, plot_type, bankroll):
    if plot_type == "expt1_fig2":
        result_array = np.zeros((1000, 1001))
        for episode in range(1000):
            result = american_roulette_simulator(win_prob, limited_bankroll=False, bankroll_amount=bankroll)
            result_array[episode] = result
        return result_array

    elif plot_type == "expt2_fig1":
        result_array = np.zeros((1000, 1001))
        # loses = 0
        # wins = 0
        for episode in range(1000):
            result = american_roulette_simulator(win_prob, limited_bankroll=True, bankroll_amount=bankroll)
            result_array[episode] = result
        #     if result[-1] == -256:
        #         loses+=1
        #     else:
        #         wins+=1
        # print(loses)
        # print(wins)
        return result_array

    else:
        print("Please choose the correct plot type")


if __name__ == "__main__":
    test_code()
