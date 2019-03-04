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
