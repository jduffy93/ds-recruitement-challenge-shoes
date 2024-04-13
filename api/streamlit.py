import streamlit as st
import xgboost as xgb
from pydantic import BaseModel

# Load the model
model = xgb.Booster()
model.load_model("xgboost_model_balanced.json")

class Item(BaseModel):
    ProductCode: str
    OriginalSaleAmountInclVAT: float
    CustomerID: str
    SaleDocumentNumber: str
    RevenueInclVAT: float
    CostPriceExclVAT: float
    BrandName: str
    ModelGroup: str
    ProductGroup: str
    Day: int
    Month: int
    Weekday: int
    Webshop: bool

# Main function
def main():
    st.title("SoleMate ReturnRater")
    st.write("Predicts the odds that an item with certain characteristics will be returned by the customer")

    # Input form
    st.sidebar.header("Input Features")
    product_code = st.sidebar.text_input("Product Code", value='1968361059464632550')
    original_sale_amount = st.sidebar.number_input("Original Sale Amount Incl VAT", value=99.95)
    customer_id = st.sidebar.text_input("Customer ID", value='-2190786785520839526')
    sale_document_number = st.sidebar.text_input("Sale Document Number", value='23995792')
    revenue_incl_vat = st.sidebar.number_input("Revenue Incl VAT", value=74.96)
    cost_price_excl_vat = st.sidebar.number_input("Cost Price Excl VAT", value=36.534515)
    brand_name = st.sidebar.text_input("Brand Name", value='3694837121284491212')
    model_group = st.sidebar.text_input("Model Group", value='3162564956579801398')
    product_group = st.sidebar.text_input("Product Group", value='-453682476182549203')
    day = st.sidebar.number_input("Day", value=30)
    month = st.sidebar.number_input("Month", value=1)
    weekday = st.sidebar.number_input("Weekday", value=4)
    webshop = st.sidebar.checkbox("Webshop")

    # Predict button
    if st.sidebar.button("Predict"):
        item = Item(
            ProductCode=product_code,
            OriginalSaleAmountInclVAT=original_sale_amount,
            CustomerID=customer_id,
            SaleDocumentNumber=sale_document_number,
            RevenueInclVAT=revenue_incl_vat,
            CostPriceExclVAT=cost_price_excl_vat,
            BrandName=brand_name,
            ModelGroup=model_group,
            ProductGroup=product_group,
            Day=day,
            Month=month,
            Weekday=weekday,
            Webshop=webshop
        )

        prediction = predict_item_return(item)
        st.write(f"The predicted odds that the item will be returned: {prediction}")

# Function to predict item return
def predict_item_return(item: Item):
    # Convert the input data to a format suitable for the model
    data = [
        item.ProductCode,
        item.OriginalSaleAmountInclVAT,
        item.CustomerID,
        item.SaleDocumentNumber,
        item.RevenueInclVAT,
        item.CostPriceExclVAT,
        item.BrandName,
        item.ModelGroup,
        item.ProductGroup,
        item.Day,
        item.Month,
        item.Weekday,
        int(item.Webshop),
    ]

    # Make the prediction using the loaded model
    prediction = model.predict([data])[0]

    return prediction

if __name__ == "__main__":
    main()
