import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Virtual DDJ-1000",
    layout="wide"
)

# --------------------------------
# ESTADO
# --------------------------------

for key, value in {
    "play_a": False,
    "play_b": False,
    "crossfader": 50,
    "bpm_a": 128.0,
    "bpm_b": 128.0,
}.items():

    if key not in st.session_state:
        st.session_state[key] = value

# --------------------------------
# CSS
# --------------------------------

st.markdown("""
<style>

.stApp{
    background:#05070b;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------
# TÍTULO
# --------------------------------

st.title("🎧 Virtual DDJ-1000")

# --------------------------------
# WAVEFORMS
# --------------------------------

wave = np.sin(
    np.linspace(
        0,
        50,
        2000
    )
)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        y=wave,
        mode="lines"
    )
)

fig.update_layout(
    height=120,
    margin=dict(
        l=0,
        r=0,
        t=0,
        b=0
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------
# FOTO CONTROLADORA
# --------------------------------

st.image(
    "assets/ddj1000.png",
    use_container_width=True
)

# --------------------------------
# DECKS
# --------------------------------

left, center, right = st.columns(
    [3,2,3]
)

with left:

    st.subheader("DECK A")

    if st.button(
        "▶ PLAY A"
    ):
        st.session_state.play_a = not st.session_state.play_a

    st.metric(
        "BPM",
        st.session_state.bpm_a
    )

    st.slider(
        "Pitch A",
        -16,
        16,
        0
    )

with center:

    st.subheader("MIXER")

    st.session_state.crossfader = st.slider(
        "Crossfader",
        0,
        100,
        st.session_state.crossfader
    )

    st.slider(
        "Master",
        0,
        100,
        75
    )

with right:

    st.subheader("DECK B")

    if st.button(
        "▶ PLAY B"
    ):
        st.session_state.play_b = not st.session_state.play_b

    st.metric(
        "BPM",
        st.session_state.bpm_b
    )

    st.slider(
        "Pitch B",
        -16,
        16,
        0
    )

# --------------------------------
# BIBLIOTECA
# --------------------------------

st.divider()

st.subheader(
    "📚 Biblioteca"
)

track = st.file_uploader(
    "Cargar tema",
    type=[
        "mp3",
        "wav",
        "flac"
    ]
)

if track:

    st.success(
        track.name
    )
