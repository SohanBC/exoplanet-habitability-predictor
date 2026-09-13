import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Exoplanet Habitability Predictor",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    model = joblib.load("exoplanet_habitability_model.pkl")
    features = joblib.load("features.pkl")
    return model, features


model, features = load_model()


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    }

    /* Main background */
    .stApp {
        background:
            radial-gradient(circle at 20% 10%, rgba(75, 45, 150, 0.18), transparent 28%),
            radial-gradient(circle at 80% 20%, rgba(0, 120, 180, 0.12), transparent 25%),
            #0b1020;
    }

    /* Main container */
    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Header */
    .hero {
        padding: 2rem 2rem 1.5rem 2rem;
        border-radius: 22px;
        background: linear-gradient(
            135deg,
            rgba(35, 45, 90, 0.95),
            rgba(13, 22, 50, 0.95)
        );
        border: 1px solid rgba(255,255,255,0.10);
        margin-bottom: 1.5rem;
        box-shadow: 0 12px 40px rgba(0,0,0,0.30);
    }

    .hero-title {
    font-size: 2.8rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1.1;
    margin-bottom: 0.6rem;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: #b9c3d6;
        font-weight: 400;
    letter-spacing: 0.01em;
        line-height: 1.6;
    }

    /* Cards */
    .card {
        padding: 1.25rem;
        border-radius: 18px;
        background: rgba(24, 32, 55, 0.78);
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 1rem;
    }

    /* Prediction cards */
    .prediction-good {
        padding: 1.8rem;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            rgba(20, 120, 80, 0.30),
            rgba(15, 70, 55, 0.38)
        );
        border: 1px solid rgba(70, 220, 160, 0.35);
        text-align: center;
        margin-bottom: 1rem;
    }

    .prediction-bad {
        padding: 1.8rem;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            rgba(150, 50, 50, 0.30),
            rgba(85, 30, 40, 0.38)
        );
        border: 1px solid rgba(240, 100, 100, 0.35);
        text-align: center;
        margin-bottom: 1rem;
    }

    .prediction-title {
        font-size: 1.8rem;
        font-weight: 750;
        margin-bottom: 0.4rem;
    }

    .probability {
        font-size: 2.8rem;
        font-weight: 800;
    }

    /* Small labels */
    .section-title {
        font-size: 1.35rem;
        font-weight: 750;
        margin-top: 0.5rem;
        margin-bottom: 0.8rem;
    }

    .small-text {
        color: #9da9bd;
        font-size: 0.9rem;
    }

    /* Hide Streamlit top decoration */
    [data-testid="stHeader"] {
        background: transparent;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #0d1428;
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    /* Button */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        font-weight: 700;
        padding: 0.7rem 1rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🌌 Exoplanet AI")

    st.caption("Habitability Potential Screening")

    st.divider()

    page = st.radio(
        "Navigate",
        ["🔭 Predictor", "📊 Model Information", "ℹ️ About Project"]
    )

    st.divider()

    st.markdown("### 🪐 Project Stats")

    st.metric("NASA planets", "6,360")
    st.metric("Features", "8")

    st.divider()

    st.caption(
        "Built using NASA Exoplanet Archive data, "
        "Python, Pandas and Scikit-learn."
    )


# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">🌌 Exoplanet Habitability Predictor</div>
        <div class="hero-subtitle">
            Explore whether an exoplanet's physical and stellar characteristics
            fall within our project's potential-habitability screening region.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PREDICTOR PAGE
# =========================================================

if page == "🔭 Predictor":

    st.markdown(
        '<div class="section-title">🔭 Enter Exoplanet Characteristics</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Tip: Start with the Earth-like preset to see an example prediction."
    )

    # -----------------------------------------------------
    # Presets
    # -----------------------------------------------------

    presets = {
        "Custom": {
            "radius": 1.0,
            "period": 365.0,
            "axis": 1.0,
            "temp": 288.0,
            "insol": 1.0,
            "star_temp": 5778.0,
            "star_mass": 1.0,
            "star_radius": 1.0
        },

        "🌍 Earth-like": {
            "radius": 1.0,
            "period": 365.0,
            "axis": 1.0,
            "temp": 288.0,
            "insol": 1.0,
            "star_temp": 5778.0,
            "star_mass": 1.0,
            "star_radius": 1.0
        },

        "🔥 Hot Jupiter": {
            "radius": 11.0,
            "period": 3.0,
            "axis": 0.04,
            "temp": 1500.0,
            "insol": 1000.0,
            "star_temp": 6000.0,
            "star_mass": 1.1,
            "star_radius": 1.2
        },

        "❄️ Cold World": {
            "radius": 1.0,
            "period": 500.0,
            "axis": 2.0,
            "temp": 150.0,
            "insol": 0.15,
            "star_temp": 5000.0,
            "star_mass": 0.8,
            "star_radius": 0.8
        }
    }

    preset = st.selectbox(
        "Quick preset",
        list(presets.keys())
    )

    values = presets[preset]

    st.divider()

    # -----------------------------------------------------
    # Planetary inputs
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">🪐 Planetary Properties</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        planet_radius = st.number_input(
            "Planet Radius (Earth radii)",
            min_value=0.01,
            value=float(values["radius"]),
            step=0.1
        )

        orbital_period = st.number_input(
            "Orbital Period (days)",
            min_value=0.01,
            value=float(values["period"]),
            step=1.0
        )

    with col2:

        semi_major_axis = st.number_input(
            "Semi-Major Axis (AU)",
            min_value=0.0001,
            value=float(values["axis"]),
            step=0.01
        )

        equilibrium_temperature = st.number_input(
            "Equilibrium Temperature (K)",
            min_value=0.0,
            value=float(values["temp"]),
            step=10.0
        )

    # -----------------------------------------------------
    # Stellar inputs
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">⭐ Stellar Environment</div>',
        unsafe_allow_html=True
    )

    col3, col4 = st.columns(2)

    with col3:

        insolation_flux = st.number_input(
            "Insolation Flux (Earth units)",
            min_value=0.0,
            value=float(values["insol"]),
            step=0.1
        )

        star_temperature = st.number_input(
            "Star Temperature (K)",
            min_value=0.0,
            value=float(values["star_temp"]),
            step=50.0
        )

    with col4:

        star_mass = st.number_input(
            "Star Mass (Solar masses)",
            min_value=0.001,
            value=float(values["star_mass"]),
            step=0.05
        )

        star_radius = st.number_input(
            "Star Radius (Solar radii)",
            min_value=0.001,
            value=float(values["star_radius"]),
            step=0.05
        )

    st.divider()

    # -----------------------------------------------------
    # Prediction button
    # -----------------------------------------------------

    predict_button = st.button(
        "🔭 Analyze Exoplanet",
        type="primary"
    )

    if predict_button:

        input_data = pd.DataFrame(
            [[
                planet_radius,
                orbital_period,
                semi_major_axis,
                equilibrium_temperature,
                insolation_flux,
                star_temperature,
                star_mass,
                star_radius
            ]],
            columns=features
        )

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        # -------------------------------------------------
        # Prediction result
        # -------------------------------------------------

        st.markdown("## Prediction Result")

        if prediction == 1:

            st.markdown(
                f"""
                <div class="prediction-good">
                    <div class="prediction-title">
                        🌍 Potentially Habitable
                    </div>
                    <div class="probability">
                        {probability:.1%}
                    </div>
                    <div class="small-text">
                        Model probability for the positive screening class
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="prediction-bad">
                    <div class="prediction-title">
                        🚫 Not Potentially Habitable
                    </div>
                    <div class="probability">
                        {probability:.1%}
                    </div>
                    <div class="small-text">
                        Model probability for the positive screening class
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        # -------------------------------------------------
        # Probability bar
        # -------------------------------------------------

        st.progress(float(probability))

        # -------------------------------------------------
        # Screening criteria
        # -------------------------------------------------

        st.markdown("### 🔬 Screening Criteria")

        criteria = {
            "Planet radius": (
                0.5 <= planet_radius <= 2.0,
                "0.5–2.0 Earth radii"
            ),

            "Equilibrium temperature": (
                200 <= equilibrium_temperature <= 350,
                "200–350 K"
            ),

            "Insolation flux": (
                0.25 <= insolation_flux <= 4.0,
                "0.25–4.0 Earth units"
            )
        }

        c1, c2, c3 = st.columns(3)

        for column, (name, (passed, expected)) in zip(
            [c1, c2, c3],
            criteria.items()
        ):

            with column:

                if passed:
                    st.success(f"✅ {name}")
                else:
                    st.error(f"❌ {name}")

                st.caption(f"Target range: {expected}")

        # -------------------------------------------------
        # Input summary
        # -------------------------------------------------

        with st.expander("📋 View Input Summary"):

            summary = pd.DataFrame({
                "Feature": [
                    "Planet Radius",
                    "Orbital Period",
                    "Semi-Major Axis",
                    "Equilibrium Temperature",
                    "Insolation Flux",
                    "Star Temperature",
                    "Star Mass",
                    "Star Radius"
                ],

                "Value": [
                    planet_radius,
                    orbital_period,
                    semi_major_axis,
                    equilibrium_temperature,
                    insolation_flux,
                    star_temperature,
                    star_mass,
                    star_radius
                ]
            })

            st.dataframe(
                summary,
                use_container_width=True,
                hide_index=True
            )

        st.caption(
            "⚠️ The result is a project-defined screening prediction. "
            "It is not evidence that life exists on the planet."
        )


# =========================================================
# MODEL INFORMATION PAGE
# =========================================================

elif page == "📊 Model Information":

    st.markdown("## 📊 Model Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Algorithm", "Random Forest")

    with col2:
        st.metric("Input Features", "8")

    with col3:
        st.metric("Training Dataset", "NASA")


    st.markdown("### 🧠 Features Used")

    feature_table = pd.DataFrame({
        "Feature": [
            "Planet Radius",
            "Orbital Period",
            "Semi-Major Axis",
            "Equilibrium Temperature",
            "Insolation Flux",
            "Star Temperature",
            "Star Mass",
            "Star Radius"
        ],

        "Role": [
            "Planet size",
            "Orbital characteristics",
            "Orbital distance",
            "Temperature environment",
            "Energy received",
            "Host-star environment",
            "Host-star properties",
            "Host-star properties"
        ]
    })

    st.dataframe(
        feature_table,
        use_container_width=True,
        hide_index=True
    )


    st.markdown("### 🌳 Why Random Forest?")

    st.write(
        """
        Random Forest was selected as the final model for this project because
        it can model non-linear relationships between planetary and stellar
        characteristics and is relatively robust to complex feature interactions.
        """
    )

    st.markdown("### ⚠️ Important Model Limitation")

    st.warning(
        """
        The target used in this project is a project-defined habitability-
        potential screening label. NASA does not provide a definitive
        binary 'habitable/not habitable' label in the dataset used here.

        Therefore, the model should be interpreted as a screening demonstration,
        not as a scientifically validated detector of extraterrestrial life.
        """
    )


# =========================================================
# ABOUT PROJECT PAGE
# =========================================================

elif page == "ℹ️ About Project":

    st.markdown("## 🌌 About the Project")

    st.write(
        """
        This project uses planetary and stellar measurements from the
        NASA Exoplanet Archive to build a machine-learning based
        habitability-potential screening application.
        """
    )

    st.markdown("### 🔄 Project Pipeline")

    pipeline = [
        "NASA Exoplanet Archive",
        "Data Cleaning",
        "Exploratory Data Analysis",
        "Feature Selection",
        "Feature Engineering",
        "Habitability Screening Criteria",
        "Machine Learning",
        "Model Evaluation",
        "Streamlit Deployment"
    ]

    for i, step in enumerate(pipeline, start=1):
        st.write(f"**{i}.** {step}")


    st.markdown("### 🛰️ Data Source")

    st.info(
        "NASA Exoplanet Archive — Planetary Systems Composite Parameters (PSCompPars)"
    )


    st.markdown("### ⚠️ Scientific Disclaimer")

    st.warning(
        """
        This application estimates whether an exoplanet falls within
        our project's predefined screening region.

        It does not prove that an exoplanet is habitable, contains water,
        contains life, or can support extraterrestrial life.
        """
    )

    st.markdown("---")

    st.caption(
        "Exoplanet Habitability Potential Predictor • "
        "Python • Pandas • Scikit-learn • Streamlit"
    )