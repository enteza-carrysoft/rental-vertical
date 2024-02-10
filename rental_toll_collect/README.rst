Rental Toll Collect
====================================================


Summary
-------

Import a CSV file from Toll Collect and invoice the costs to customers.

Description
-----------

This module provides the opportunity to import csv files downloaded from toll collect portal.
During import it matches the given license plate in csv file with a vehicle product.
The toll charge lines can be invoiced to a customer manually or by creating an invoice from a 
sale/rental order containing a vehicle product as sale/rental order line.

The csv should contain the following columns:

- Account number ("Mautaufstellungs-Nr.")
- license plate ("Kfz-Kennz.")
- Date ("Datum")
- Start ("Start")
- Booking number ("Buchungsnummer")
- Type ("Art")
- Route Ramp ("Auffahrt")
- Route Via ("über")
- Route Exit ("Abfahrt")
- Analytic Account ("Kostenstelle")
- Tariff Model ("Tarifmodell")
- Axle class ("Achsklasse")
- Weight class ("Gewichtsklasse")
- Polution class ("Schadstoffklasse")
- Road operator ("Straßenbetreiber")
- Procedure ("Verf.¹")
- Distance ("km")
- Amount ("EUR")


Usage
-----

-  Go to Rentals > Configuration > Settings
- Activate the automatic invoicing of toll charges if toll charges should be automatically invoiced together with rental services.
- Create a rental order with vehicle products as rental order lines.
- Confirm the rental order.
- Go to Rentals > Product > Toll Charges > Import Toll Charges.
- Upload your csv file and import the file.
- Go to Rentals > Product > Toll Charges > Toll Charge Lines and see all imported toll charge lines.
- Go to a vehicle product and click on smartbutton for toll charges and see all related toll charge lines.
- Go back to the rental order and create an invoice.
- If the date of the toll charge lines match the service period of rental order lines,
  a new invoice line is additionally added for each vehicle product with distance and amount.

- Mark one or several toll charge lines in tree view and create an invoice via action wizard to invoice them manually.

