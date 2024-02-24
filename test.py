 

# I want to code a function to calculate the bond yield to maturity

def bond_yield_to_maturity(coupon, face_value, years_to_maturity, current_price):
    # coupon is the coupon rate
    # face_value is the face value of the bond
    # years_to_maturity is the number of years to maturity
    # current_price is the current price of the bond
    # calculate the bond yield to maturity
    # formula is (coupon + (face_value - current_price)/years_to_maturity)/((face_value + current_price)/2)
    bond_yield_to_maturity = (coupon + (face_value - current_price)/years_to_maturity)/((face_value + current_price)/2)
    return bond_yield_to_maturity

print(bond_yield_to_maturity(0.05, 100, 5, 95))












