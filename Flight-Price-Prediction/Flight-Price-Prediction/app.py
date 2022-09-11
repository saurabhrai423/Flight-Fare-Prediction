import streamlit as st
import datetime
import pandas as pd

from Flight_Price_Predict import predict

'''
# Flight Price Prediction
Fill the necessary details and get approx price. 
'''
airline = ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet', 'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia', 'Vistara Premium economy', 'Jet Airways Business',
           'Multiple carriers Premium economy', 'Trujet']
source = ['Kolkata', 'Delhi', 'Chennai', 'Mumbai', 'Banglore']
destination = ['Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad']
stop = [0, 1, 2, 3, 4]

airline = st.selectbox("Select Airline", airline)
source = st.selectbox("Select Source", source)
destination = st.selectbox("Select Destination", destination)
total_stop = st.selectbox('Select Number of Stop', stop)

date_of_journey = st.date_input('Select Date of Journey')
journey_time = st.time_input("Journey time is", datetime.time())

date_of_arrival = st.date_input('Select Date of Arrival')
arrival_time = st.time_input('Arrival Time', datetime.time())
startTime = datetime.datetime.combine(date_of_journey, journey_time)
arrivalTime = datetime.datetime.combine(date_of_arrival, arrival_time)
total_difference = (arrivalTime - startTime).total_seconds()
print('total_difference : ', total_difference)
duration = str(int(total_difference / 3600)) + 'h ' + str(int((total_difference % 3600)%60)) + 'm'


def time_difference_check():
    flag = True
    if total_difference / 60 <= 30:
        st.error('Arrival and Start datetime should have atleast 30 minute gap')
        flag = False
    elif date_of_arrival < date_of_journey:
        st.error('Please select a proper date range')
        flag = False
    return flag
    return flag


if st.button('Predict Price'):
    # print('Airline : ',airline)
    # print('Source :',source)
    # print('Destination : ',destination)
    # print('total stop : ',total_stop)
    # print('date of journey : ',date_of_journey)
    # print(date_of_journey.day)
    # print('journey time : ',type(journey_time))
    # print('date of arrival : ',date_of_arrival)
    # print('arrival time : ',arrival_time)
    flag = time_difference_check()
    if flag == True:
        predicted_value = predict(airline, date_of_journey, source, destination, journey_time, arrival_time, duration, total_stop)
        st.write('Predicted Price is ', int(predicted_value))