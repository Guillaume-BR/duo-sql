import logging
import os
import streamlit as st
import pandas as pd
import duckdb
from datetime import datetime, timedelta

# -----------------------------------------------
# PAGE CONFIG
# -----------------------------------------------
st.set_page_config(
    page_title="DuoSQL",
    page_icon="🗄️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------
# CUSTOM CSS
# -----------------------------------------------

st.markdown("""
<style>
/* Primary button */
.stButton > button[kind="primary"],
.stButton > button {
    background: linear-gradient(135deg, #7c6fff 0%, #615fff 50%, #4f4bcc 100%);
    color: #ffffff;
    border: 1px solid #7c6fff;
    border-radius: 10px;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 500;
    letter-spacing: 0.02em;
    padding: 0.45rem 1.2rem;
    transition: all 0.18s ease;
    box-shadow: 0 0 12px rgba(97, 95, 255, 0.35), 0 2px 8px rgba(0,0,0,0.3);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #8d83ff 0%, #7c6fff 50%, #615fff 100%);
    border-color: #9d94ff;
    box-shadow: 0 0 20px rgba(97, 95, 255, 0.55), 0 4px 12px rgba(0,0,0,0.35);
    transform: translateY(-1px);
}

.stButton > button:active {
    transform: translateY(0px);
    box-shadow: 0 0 8px rgba(97, 95, 255, 0.4);
}

/* Secondary button */
.stButton > button[kind="secondary"] {
    background: transparent;
    color: #a5a3ff;
    border: 1px solid #314158;
    box-shadow: none;
}

.stButton > button[kind="secondary"]:hover {
    border-color: #615fff;
    color: #ffffff;
    box-shadow: 0 0 10px rgba(97, 95, 255, 0.25);
    transform: translateY(-1px);
}

/* ---- Badge pill ---- */
.theme-badge {
    display: inline-block;
    background: linear-gradient(135deg, #1e1a2e, #1a1e2e);
    border: 1px solid #3a3a5a;
    color: #a78bfa;
    font-family: 'Space Mono', monospace;
    font-size: 1rem;
    padding: 0.2rem 0.7rem;
    border-radius: 20px;
    letter-spacing: 0.06em;
    margin-bottom: 1rem;
}           

/* ---- Consigne header ---- */
.consigne-box {
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    border-left: 4px solid #a78bfa;
    border-radius: 0 12px 12px 0;
    padding: 1.2rem 1.6rem;
    margin: 1rem 0 1.8rem 0;
    font-size: 1.15rem;
    font-weight: 600;
    color: #ddd8ff;
    letter-spacing: 0.01em;
}
</style>
""", unsafe_allow_html=True)

# Set up logging
if "data" not in os.listdir():
    logging.error("os.listdir()")
    logging.error("Creating data/ folder")
    os.mkdir("data")

if "bdd" not in os.listdir():
    logging.error("os.listdir()")
    logging.error("Creating bdd/ folder")
    os.mkdir("bdd")

if "sql_exercices.duckdb" not in os.listdir("bdd"):
    logging.error("os.listdir('bdd/')")
    logging.error("Creating bdd/sql_exercices.duckdb database")
    exec(open("init_db.py").read())
    # subprocess.run(["python", "init_db.py"])

if "db_initialized" not in st.session_state:
    exec(open("init_db.py").read())
    st.session_state["db_initialized"] = True

if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""


# -----------------------------------------------
# FUNCTIONS
# -----------------------------------------------
def verify_sql_results(sql_query: str) -> None:
    try:
        result = con.execute(sql_query).df()
        st.dataframe(result, use_container_width=True)
    except Exception as e:
        st.warning(f"⚠️ Erreur dans ta requête SQL : `{e}`")
        return

    try:
        result = result[solution_df.columns]
        diff = result.compare(solution_df)
        if diff.empty:
            st.success("✅ Parfait ! Ta requête correspond exactement à la solution.")
        else:
            st.warning("🔍 Presque ! Voici les différences avec la solution :")
            st.dataframe(diff, use_container_width=True)
    except KeyError:
        st.error("❌ Certaines colonnes sont manquantes dans ta requête.")

    n_lines_diff = result.shape[0] - solution_df.shape[0]
    if n_lines_diff != 0:
        st.warning(f"📏 Nombre de lignes différent de la solution : **{abs(n_lines_diff)}** ligne(s) en {'trop' if n_lines_diff > 0 else 'moins'}.")


con = duckdb.connect(database="bdd/sql_exercices.duckdb", read_only=False)

st.markdown(
    """# Duo SQL App \n
        Pratiquez le SQL et progressez grâce au système de répétition espacée !
    """
)

# -----------------------------------------------
# SIDEBAR
# -----------------------------------------------
with st.sidebar:
    if st.session_state.get("reset_theme"):
        st.session_state["selected_theme"] = None
        st.session_state["reset_theme"] = False

    st.markdown("<div class='sidebar-label'>Thème</div>", unsafe_allow_html=True)
    available_themes = con.execute("SELECT DISTINCT theme FROM memory_state").df()
    option = st.selectbox(
        "Que veux-tu réviser ?",
        sorted(available_themes["theme"].unique()),
        placeholder="Choisir un thème...",
        key="selected_theme",
    )

    if option:
        select_exercise_query = f"SELECT * FROM memory_state WHERE theme = '{option}'"
    else:
        select_exercise_query = "SELECT * FROM memory_state"

    exercice = (
        con.execute(select_exercise_query)
        .df()
        .sort_values("last_reviewed")
        .reset_index(drop=True)
    )

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-label'>File d'attente</div>", unsafe_allow_html=True)

    # Afficher la liste des exercices avec leur date
    for i, row in exercice.iterrows():
        is_current = i == 0
        color = "#a78bfa" if is_current else "#3a3a5a"
        name_display = row["exercice_name"].replace("_", " ").title()
        date_display = str(row["last_reviewed"])[:10]
        st.markdown(f"""
        <div style='padding:0.5rem 0.7rem; margin-bottom:0.3rem; border-radius:8px;
                    border-left: 3px solid {color};
                    background: {"#1c1c2e" if is_current else "transparent"};
                    font-family: Space Mono, monospace; font-size:0.72rem;'>
            <span style='color:{"#e8e8f0" if is_current else "#4a4a6a"};'>{name_display}</span><br>
            <span style='color:#3a3a5a;'>{date_display}</span>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------
# EXERCISE
# -----------------------------------------------
exercice_name = exercice.loc[0, "exercice_name"]
with open(f"answers/{exercice_name}.sql", "r") as file:
    ANSWER = file.read()

solution_df = con.execute(ANSWER).df()
consigne = exercice.loc[0, "consigne"]
theme = exercice.loc[0, "theme"]

st.markdown(f"<div class='theme-badge'>📚 {theme}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='consigne-box'>💬 {consigne}</div>", unsafe_allow_html=True)

# -----------------------------------------------
# SPACED REPETITION BUTTONS
# -----------------------------------------------
col1, col2, col3, col4 = st.columns([2, 2, 2, 1])

for col, days, emoji in zip([col1, col2, col3], [2, 7, 21], ["⚡", "📅", "🗓️"]):
    if col.button(f"{emoji} Revoir dans {days} jours", use_container_width=True):
        next_review = datetime.now() + timedelta(days=days)
        con.execute(
            f"UPDATE memory_state SET last_reviewed = '{next_review}' WHERE exercice_name = '{exercice_name}'"
        )
        st.session_state["user_input"] = ""
        st.session_state["reset_theme"] = True
        st.rerun()

if col4.button("↺ Reset", use_container_width=True):
    con.execute(
        f"UPDATE memory_state SET last_reviewed = '2000-01-01' WHERE exercice_name = '{exercice_name}'"
    )
    st.session_state["user_input"] = ""
    st.session_state["reset_theme"] = True
    st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------
# SQL INPUT
# -----------------------------------------------
query_user = st.text_area(
    "✏️ Votre requête SQL",
    key="user_input",
    height=160,
    placeholder="SELECT * FROM ...",
)

if query_user:
    verify_sql_results(query_user)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------
# TABS
# -----------------------------------------------
tab2, tab3 = st.tabs(["📋  Tables disponibles", "💡  Solution"])

with tab2:
    exercice_tables = exercice.loc[0, "tables"]
    cols = st.columns(len(exercice_tables)) if len(exercice_tables) > 1 else [st.container()]
    for col, table in zip(cols, exercice_tables):
        with col:
            st.markdown(f"<div class='sidebar-label'>{table}</div>", unsafe_allow_html=True)
            df_table = con.execute(f"SELECT * FROM {table}").df()
            st.dataframe(df_table, use_container_width=True)

with tab3:
    if not query_user:
        st.warning("💪 Essaie quelque chose avant de regarder la solution !")
    else:
        st.code(ANSWER, language="sql")
