#!/usr/bin/env bash

# import recent data for FMCSA Census update path of heave file to input records
mongoimport -d smsdbRecent -c MotorCarrier --type csv --file FMCSA_CENSUS/fmcsa_census_lite.csv --headerline

# import recent data for active Motor carriers for Hazmat
#mongoimport -d smsdbRecent -c activeMotorsHazmat --type csv --file SMS_ACTIVE_MOTORCARRIER/hazmat/active_hazmat_motor_carrier_lite.csv --headerline

# import recent data for active Motor carriers for non Hazmat
#mongoimport -d smsdbRecent -c activeMotorsNonHazmat --type csv --file SMS_ACTIVE_MOTORCARRIER/nonHazmat/active_non_hazmat_motor_carrier_lite.csv --headerline


