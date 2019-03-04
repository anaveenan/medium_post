#part 1
import numpy as np
import scipy.stats as st
# Initialize delta(minimum lift the product manager expect), control_mean, control_sd
delta=0.05
control_mean=2
control_sd=1
sample_size=1000
alpha=0.05#significance of the experiment
n_sim=1000#Total number of samples to simulate

np.random.seed(123)#set seed
def simulate_data(control_mean,control_sd,sample_size,n_sim):
    # Simulate the time spend under null hypothesis
    control_time_spent = np.random.normal(loc=control_mean, scale=control_sd, size=(sample_size,n_sim))
    # Simulate the time spend under alternate hypothesis
    treatment_time_spent = np.random.normal(loc=control_mean*(1+delta), scale=control_sd, size=(sample_size,n_sim))
    return control_time_spent,treatment_time_spent
# Run the t-test and get the p_value
control_time_spent, treatment_time_spent=simulate_data(control_mean,control_sd,sample_size,n_sim)
t_stat, p_value = st.ttest_ind(control_time_spent, treatment_time_spent)
power=(p_value<0.05).sum()/n_sim
print("Power of the experiment {:.1%}".format(power))
#Power of the experiment 58.8%


#part 2
#increment sample size till required power is reached 
sample_size=1000
np.random.seed(123)
while True:
    control_time_spent, treatment_time_spent=simulate_data(control_mean,control_sd,sample_size,n_sim)
    t_stat, p_value = st.ttest_ind(control_time_spent, treatment_time_spent)
    power=(p_value<alpha).sum()/n_sim
    if power>.80:
        print("Minimum sample size required to reach significance {}".format(sample_size))
        break
    else:
        sample_size+=10
#Minimum sample size required to reach significance 1560


#part 3
#Analtyical solution to compute sample size
from statsmodels.stats.power import tt_ind_solve_power

treat_mean=control_mean*(1+delta)
mean_diff=treat_mean-control_mean

cohen_d=mean_diff/np.sqrt((control_sd**2+control_sd**2)/2)

n = tt_ind_solve_power(effect_size=cohen_d, alpha=alpha, power=0.8, ratio=1, alternative='two-sided')
print('Minimum sample size required to reach significance: {:.0f}'.format(round(n)))
#minimum sample size required to reach significance: 1571
