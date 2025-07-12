import streamlit as st

st.title("🫖 Chai Pe Charcha - Chai Bill 🫖")

# Prices
single_T = 15
full_T = 20
W_500ml = 10
W_1000ml = 20

st.header("Tea Section")
single_tea = st.number_input("Number of Single Teas (₹15 each):", min_value=0, step=1)
full_tea = st.number_input("Number of Full Teas (₹20 each):", min_value=0, step=1)

st.header("Biscuits Section (3 for ₹10)")
biscuits = st.number_input("Number of Biscuits:", min_value=0, step=1)

st.header("Water Bottles")
water_bottles = st.number_input("Number of Water Bottles:", min_value=0, step=1)

water_total = 0
bottle_sizes = []

for i in range(water_bottles):
    size = st.selectbox(f"Bottle {i+1} size (ml):", [500, 1000], key=f"bottle_{i}")
    bottle_sizes.append(size)
    if size == 500:
        water_total += W_500ml
    else:
        water_total += W_1000ml

# Tea calculation
tea_total = (single_tea * single_T) + (full_tea * full_T)

# Biscuit calculation
full_sets = biscuits // 3
remaining = biscuits % 3
biscuit_total = (full_sets * 10) + round((remaining * 10) / 3)

# Final total
total = tea_total + biscuit_total + water_total

if st.button("Calculate Total"):
    st.subheader("🧾 Bill Summary")
    st.write(f"Tea Amount: ₹{tea_total}")
    st.write(f"Biscuit Amount ({biscuits}): ₹{biscuit_total}")
    st.write(f"Water Bottle Amount ({water_bottles} bottles): ₹{water_total}")
    st.success(f"Total Bill: ₹{round(total)}")
