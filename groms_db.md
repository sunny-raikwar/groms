	***Land Detail***
Land Id
Belonging to 
P.H No.
K.H No./Survey No.
Mouza /village
Panchayat
Thesil
District
Taluka
Irrigation
Broker Name
Purchase Date
Total Area (in acres)
Rate/Acres
total Cost
Reg. Date
Amount
Adv Amt (Cheque)
Description


***Layout Details***
land Id (foreign Key)
Layout ID
Layout Name
Remark
Date
Area under Layout
Area under possession
Area unser plots
Area under open space
Area under Public utility
Area under roads

***Plot Details***
Layout ID (FK)
Date
plot id
plot no.
total area of plot
tan area of plot
net area of plot
status
Remark
plot category (FK)

***Plot Category***
category id
detail / description
length
width
Rate
Remark
Project id(FK)

***Project Detail***
project id
land id(FK)
layout id(FK)
project name
description

***Booking Detail***
booking id
type
customer id(FK)
plot id(FK)
Project id(FK)
agent id(FK)
Remark
card num.
B Mode
total cost
discount
nett cost
Token amount
paid amount
Discount installment
penality
other charge
balance
commision rate id(FK)

***Customer Detail***
customer id
name
age
gender
address
email
contact no.
alternate contact
date
pan card

***nomini Detail***
nomini id
name
age
gender
relation
address
contact num.
email
belongto(customer/agent)

***Commision Rate***
commision id
executive id(FK)
plot id(FK)
new rate
old rate
date
new amount
old amount 
change
remark

***Agent Detail***
agent id
full name(first, middle, last)
father name
mother name
pan card
address
DOB
Contact num.
Alternate Contact num.
Email
Date of Joining
Percentage Alotted
Max Percentage
Nomini id(Fk)
type id(FK)
Introducer id(FK)
Introducer percentage
account id

***Receipt***
receipt id/number
amount

***staff***
full name
contact no.
id 
password
address
