import streamlit as st
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Setup backend import
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from backend.magic_tools import list_files, ensure_dir

# Auth check
if not st.session_state.get("authenticated"):
    st.warning("Please log in to access analytics.")
    st.stop()

st.title("Analytics Dashboard 2.0")

# Paths
ENTRIES_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "entries"))
UPLOADS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "uploads"))

# Ensure directories exist
ensure_dir(ENTRIES_DIR)
ensure_dir(UPLOADS_DIR)

def extract_date(file):
    try:
        parts = file.split("_")
        date_part = parts[1]  # e.g. 2025-08-04
        return datetime.strptime(date_part, "%Y-%m-%d").date()
    except:
        return None

# Gather data
entry_dates = [extract_date(f) for f in list_files(ENTRIES_DIR, ".txt")]
upload_dates = [extract_date(f) for f in list_files(UPLOADS_DIR)]

# Convert to DataFrame
entry_df = pd.DataFrame({"date": entry_dates}).dropna()
upload_df = pd.DataFrame({"date": upload_dates}).dropna()

# Date filter
today = datetime.now().date()
default_start = today - timedelta(days=30)
start_date, end_date = st.date_input("Filter by date range", (default_start, today))

# Apply filter
filtered_entries = entry_df[(entry_df["date"] >= start_date) & (entry_df["date"] <= end_date)]
filtered_uploads = upload_df[(upload_df["date"] >= start_date) & (upload_df["date"] <= end_date)]

entry_counts = filtered_entries.groupby("date").size()
upload_counts = filtered_uploads.groupby("date").size()

# Chart 1: Diary Entries Per Day
st.subheader("Diary Entries Per Day")
if entry_counts.empty:
    st.info("No entries during selected date range.")
else:
    fig1, ax1 = plt.subplots()
    entry_counts.plot(kind="bar", ax=ax1, color="#4CAF50")
    ax1.set_ylabel("Number of Entries")
    st.pyplot(fig1)

# Chart 2: Uploads Per Day
st.subheader("File Uploads Per Day")
if upload_counts.empty:
    st.info("No uploads during selected date range.")
else:
    fig2, ax2 = plt.subplots()
    upload_counts.plot(kind="bar", ax=ax2, color="#2196F3")
    ax2.set_ylabel("Number of Uploads")
    st.pyplot(fig2)

# Summary
st.subheader("Summary")
st.markdown(f"**Total Diary Entries:** {len(filtered_entries)}")
st.markdown(f"**Total File Uploads:** {len(filtered_uploads)}")
