# Simple probability example

P_rain = 0.2
P_wet_given_rain = 0.9
P_wet_given_no_rain = 0.1

P_wet = (P_rain * P_wet_given_rain) + ((1-P_rain) * P_wet_given_no_rain)

print("Probability of wet grass:", P_wet)
