import statsmodels.api as sm
import matplotlib.pyplot as plt


def fahrenheit_to_celsius(temp):
    """Convert temperature in fahrenheit to celsius.
    
    Parameters
    ----------
    temp : float or array_like
        Temperature(s) in fahrenheit.
        
    Returns
    -------
    float or array_like
        Temperatures in celsius.

    bubbles
    
    """
    try:
        newtemps = (temp - 32) * 5/9
    except TypeError:
        newtemps = []
        for value in temp:
            newtemps.append(fahrenheit_to_celsius(value))

    return newtemps


def analyze(data):
    """Return panel plot of mosquito population vs. temperature, rainfall.
    
    Also prints t-values for temperature and rainfall.
    
    Panel plot gives: 
        1. comparison of modeled values of mosquito population vs. actual values
        2. mosquito population vs. average temperature
        3. mosquito population vs. total rainfall
    
    Parameters
    ----------
    data : DataFrame
        DataFrame giving columns for average temperature, 
        total rainfall, and mosquito population during mosquito
        breeding season for each year.
    
    Returns
    -------
    Figure
        :mod:`matplotlib.figure.Figure` object giving panel plot.
    
    """
    # perform fit
    regr_results = sm.OLS.from_formula('mosquitos ~ temperature + rainfall', data).fit()
    print(regr_results.tvalues)
    
    fig = plt.figure(figsize=(6, 9))

    # plot prediction from fitted model against measured mosquito population
    parameters = regr_results.params
    predicted = parameters['Intercept'] + parameters['temperature'] * data['temperature'] + parameters['rainfall'] * data['rainfall']
    
    ax0 = fig.add_subplot(3, 1, 1)
    ax0.plot(predicted, data['mosquitos'], 'go')
    
    ax0.set_xlabel('predicted mosquito population')
    ax0.set_ylabel('measured mosquito population')
   
    # plot population vs. temperature
    ax1 = fig.add_subplot(3, 1, 2)

    ax1.plot(data['temperature'], data['mosquitos'], 'ro')
    ax1.set_xlabel('Temperature')
    ax1.set_ylabel('Mosquitos')

    # plot population vs. rainfall
    ax2 = fig.add_subplot(3, 1, 3)

    ax2.plot(data['rainfall'], data['mosquitos'], 'bs')

    ax2.set_xlabel('Rainfall')
    ax2.set_ylabel('Mosquitos')

    return fig
