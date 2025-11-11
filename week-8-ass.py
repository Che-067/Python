# cord19_analysis.py
"""
CORD-19 Dataset Analysis
Part 1: Data Loading and Basic Exploration
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

print("=== PART 1: DATA LOADING AND BASIC EXPLORATION ===\n")

# Download and load the data
try:
    df = pd.read_csv(r"C:\Users\DELL\Downloads\python programs\metadata.csv")
    print("✓ Successfully loaded metadata.csv")
except FileNotFoundError:
    print("❌ Error: metadata.csv not found.")
    exit()

# ... [Your existing Part 1 code] ...

# === ADD PART 2 HERE ===
print("\n\n=== PART 2: DATA CLEANING AND PREPARATION ===\n")

# Create a copy for cleaning - THIS CREATES df_clean!
df_clean = df.copy()
initial_count = len(df_clean)

print("1. HANDLING MISSING DATA:")

# Remove records with missing titles
df_clean = df_clean.dropna(subset=['title'])
print(f"  - Removed {initial_count - len(df_clean)} records with missing titles")

# Fill important columns
df_clean['abstract'] = df_clean['abstract'].fillna('No abstract available')
df_clean['authors'] = df_clean['authors'].fillna('Unknown authors')
df_clean['journal'] = df_clean['journal'].fillna('Unknown journal')
df_clean['source_x'] = df_clean['source_x'].fillna('Unknown source')

# Create new features
df_clean['publish_time_parsed'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
df_clean['publication_year'] = df_clean['publish_time_parsed'].dt.year
df_clean['abstract_word_count'] = df_clean['abstract'].apply(
    lambda x: len(str(x).split()) if x != 'No abstract available' else 0
)
df_clean['title_word_count'] = df_clean['title'].apply(lambda x: len(str(x).split()))
df_clean['has_abstract'] = df_clean['abstract'] != 'No abstract available'

print(f"Final cleaned dataset: {len(df_clean)} records")

# === THEN CONTINUE WITH PART 3 ===
print("\n\n=== PART 3: DATA ANALYSIS AND VISUALIZATION ===\n")

# Now df_clean exists and you can use it!
yearly_counts = df_clean['publication_year'].value_counts().sort_index()
print("Publications by year:")
for year, count in yearly_counts.items():
    print(f"  {year}: {count} papers")

# Continue in the same file
print("\n\n=== PART 3: DATA ANALYSIS AND VISUALIZATION ===\n")

# Set up visualization style
plt.style.use('default')
sns.set_palette("husl")

print("1. PERFORMING BASIC ANALYSIS:")

# Count papers by publication year
yearly_counts = df_clean['publication_year'].value_counts().sort_index()
print("Publications by year:")
for year, count in yearly_counts.items():
    print(f"  {year}: {count} papers")

# Identify top journals publishing COVID-19 research
top_journals = df_clean['journal'].value_counts().head(10)
print("\nTop 10 journals by publication count:")
for i, (journal, count) in enumerate(top_journals.items(), 1):
    print(f"  {i:2}. {journal}: {count} papers")

# Find most frequent words in titles (using simple word frequency)
def get_top_words(text_series, n=20, exclude_words=None):
    """Extract top n most frequent words from text series"""
    if exclude_words is None:
        exclude_words = {'the', 'and', 'of', 'in', 'to', 'a', 'for', 'with', 'on', 'as'}
    
    all_words = []
    for text in text_series:
        if pd.notna(text):
            # Simple cleaning: lowercase, alphanumeric, min 3 chars
            words = re.findall(r'\b[a-zA-Z]{3,}\b', str(text).lower())
            filtered_words = [word for word in words if word not in exclude_words]
            all_words.extend(filtered_words)
    
    return Counter(all_words).most_common(n)

top_title_words = get_top_words(df_clean['title'])
print("\nTop 20 words in paper titles (excluding common words):")
for word, count in top_title_words:
    print(f"  {word:15}: {count:4} occurrences")

print("\n2. CREATING VISUALIZATIONS:")

# Create a comprehensive visualization dashboard
fig = plt.figure(figsize=(18, 12))

# Plot 1: Number of publications over time
plt.subplot(2, 3, 1)
yearly_counts_filtered = yearly_counts[yearly_counts.index >= 2019]  # Focus on recent years
plt.bar(yearly_counts_filtered.index, yearly_counts_filtered.values, 
        color='skyblue', edgecolor='navy', alpha=0.7)
plt.title('Publications by Year (2019+)', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.grid(True, alpha=0.3)

# Plot 2: Bar chart of top publishing journals
plt.subplot(2, 3, 2)
top_journals_vis = top_journals.head(8)
plt.barh(range(len(top_journals_vis)), top_journals_vis.values, 
         color='lightgreen', edgecolor='darkgreen')
plt.yticks(range(len(top_journals_vis)), 
           [j[:30] + '...' if len(j) > 30 else j for j in top_journals_vis.index])
plt.title('Top 8 Publishing Journals', fontweight='bold')
plt.xlabel('Number of Publications')
plt.gca().invert_yaxis()

# Plot 3: Distribution of paper counts by source
plt.subplot(2, 3, 3)
top_sources = df_clean['source_x'].value_counts().head(8)
plt.bar(range(len(top_sources)), top_sources.values, 
        color='orange', alpha=0.7, edgecolor='darkorange')
plt.xticks(range(len(top_sources)), top_sources.index, rotation=45, ha='right')
plt.title('Top 8 Sources by Publication Count', fontweight='bold')
plt.ylabel('Number of Publications')

# Plot 4: Abstract word count distribution
plt.subplot(2, 3, 4)
abstract_lengths = df_clean[df_clean['abstract_word_count'] <= 1000]['abstract_word_count']
plt.hist(abstract_lengths, bins=50, alpha=0.7, color='purple', edgecolor='black')
plt.title('Distribution of Abstract Lengths', fontweight='bold')
plt.xlabel('Word Count')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)

# Plot 5: Abstract availability
plt.subplot(2, 3, 5)
abstract_availability = df_clean['has_abstract'].value_counts()
plt.pie(abstract_availability.values, labels=['With Abstract', 'Without Abstract'], 
        autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
plt.title('Abstract Availability', fontweight='bold')

# Plot 6: Top words in titles
plt.subplot(2, 3, 6)
top_words_vis = top_title_words[:10]  # Top 10 words
words, counts = zip(*top_words_vis)
plt.barh(range(len(words)), counts, color='cyan', alpha=0.7)
plt.yticks(range(len(words)), words)
plt.title('Top 10 Words in Titles', fontweight='bold')
plt.xlabel('Frequency')
plt.gca().invert_yaxis()

plt.tight_layout()
plt.savefig('cord19_analysis_results.png', dpi=300, bbox_inches='tight')
plt.show()

print("✓ Visualizations saved as 'cord19_analysis_results.png'")

# Summary statistics
print("\n3. SUMMARY STATISTICS:")
print(f"Total papers analyzed: {len(df_clean):,}")
print(f"Time range: {df_clean['publication_year'].min()} - {df_clean['publication_year'].max()}")
print(f"Average abstract length: {df_clean['abstract_word_count'].mean():.1f} words")
print(f"Average title length: {df_clean['title_word_count'].mean():.1f} words")
print(f"Papers with abstracts: {df_clean['has_abstract'].sum():,} ({df_clean['has_abstract'].mean()*100:.1f}%)")

# Save cleaned dataset
df_clean.to_csv('cord19_cleaned.csv', index=False)
print("✓ Cleaned dataset saved as 'cord19_cleaned.csv'")


# app.py
"""
CORD-19 Data Explorer - Streamlit Application
Part 4: Interactive Web Application
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="CORD-19 Research Explorer",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Application title and description
st.title("🔬 CORD-19 Research Papers Explorer")
st.markdown("""
Explore the COVID-19 Open Research Dataset (CORD-19) containing scientific papers 
about COVID-19 and coronavirus research.
""")

# Load the cleaned data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(r"C:\Users\DELL\Downloads\python programs\metadata.csv")
        return df
    except FileNotFoundError:
        st.error("Cleaned dataset not found. Please run the analysis script first.")
        return None

df = load_data()

if df is not None:
    # Sidebar with interactive widgets
    st.sidebar.header("🔍 Filters & Controls")
    
    # Year range slider
    years = sorted(df['publication_year'].dropna().unique())
    if len(years) > 0:
        year_range = st.sidebar.slider(
            "Select Publication Year Range",
            min_value=int(min(years)),
            max_value=int(max(years)),
            value=(int(min(years)), int(max(years)))
        )
    else:
        year_range = (2019, 2022)
        st.sidebar.warning("No valid years found in data")
    
    # Journal selection
    journals = ['All'] + df['journal'].value_counts().head(20).index.tolist()
    selected_journal = st.sidebar.selectbox("Filter by Journal", journals)
    
    # Abstract availability filter
    abstract_filter = st.sidebar.radio("Abstract Availability", ["All", "With Abstract", "Without Abstract"])
    
    # Source selection
    sources = ['All'] + df['source_x'].value_counts().head(10).index.tolist()
    selected_source = st.sidebar.selectbox("Filter by Source", sources)
    
    # Apply filters
    filtered_df = df.copy()
    filtered_df = filtered_df[
        (filtered_df['publication_year'] >= year_range[0]) & 
        (filtered_df['publication_year'] <= year_range[1])
    ]
    
    if selected_journal != 'All':
        filtered_df = filtered_df[filtered_df['journal'] == selected_journal]
    
    if selected_source != 'All':
        filtered_df = filtered_df[filtered_df['source_x'] == selected_source]
    
    if abstract_filter == "With Abstract":
        filtered_df = filtered_df[filtered_df['has_abstract'] == True]
    elif abstract_filter == "Without Abstract":
        filtered_df = filtered_df[filtered_df['has_abstract'] == False]
    
    # Main content area
    st.header("📊 Dataset Overview")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Papers", f"{len(filtered_df):,}")
    with col2:
        st.metric("With Abstracts", f"{filtered_df['has_abstract'].sum():,}")
    with col3:
        st.metric("Unique Journals", f"{filtered_df['journal'].nunique():,}")
    with col4:
        st.metric("Date Range", f"{filtered_df['publication_year'].min()}-{filtered_df['publication_year'].max()}")
    
    # Visualization section
    st.header("📈 Data Visualizations")
    
    # Create tabs for different visualizations
    tab1, tab2, tab3, tab4 = st.tabs(["Publications Timeline", "Journal Analysis", "Source Analysis", "Data Quality"])
    
    with tab1:
        st.subheader("Publications Over Time")
        
        if len(filtered_df) > 0:
            yearly_counts = filtered_df['publication_year'].value_counts().sort_index()
            
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.bar(yearly_counts.index, yearly_counts.values, 
                   color='#1f77b4', alpha=0.7, edgecolor='darkblue')
            ax.set_xlabel('Year')
            ax.set_ylabel('Number of Publications')
            ax.set_title('Publications by Year')
            ax.grid(True, alpha=0.3)
            
            st.pyplot(fig)
        else:
            st.warning("No data available for the selected filters.")
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Top Journals")
            if len(filtered_df) > 0:
                top_journals = filtered_df['journal'].value_counts().head(10)
                
                fig, ax = plt.subplots(figsize=(8, 6))
                colors = plt.cm.Set3(np.linspace(0, 1, len(top_journals)))
                ax.barh(range(len(top_journals)), top_journals.values, color=colors)
                ax.set_yticks(range(len(top_journals)))
                ax.set_yticklabels([j[:35] + '...' if len(j) > 35 else j for j in top_journals.index])
                ax.set_xlabel('Number of Publications')
                ax.set_title('Top 10 Journals')
                ax.invert_yaxis()
                
                st.pyplot(fig)
        
        with col2:
            st.subheader("Abstract Length Distribution")
            if len(filtered_df) > 0:
                abstract_lengths = filtered_df[filtered_df['abstract_word_count'] > 0]['abstract_word_count']
                
                fig, ax = plt.subplots(figsize=(8, 4))
                ax.hist(abstract_lengths[abstract_lengths <= 1000], bins=30, 
                       alpha=0.7, color='green', edgecolor='black')
                ax.set_xlabel('Abstract Word Count')
                ax.set_ylabel('Frequency')
                ax.set_title('Distribution of Abstract Lengths')
                ax.grid(True, alpha=0.3)
                
                st.pyplot(fig)
    
    with tab3:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Publications by Source")
            if len(filtered_df) > 0:
                source_counts = filtered_df['source_x'].value_counts().head(8)
                
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.pie(source_counts.values, labels=source_counts.index, 
                      autopct='%1.1f%%', startangle=90)
                ax.set_title('Publications by Source')
                
                st.pyplot(fig)
        
        with col2:
            st.subheader("License Distribution")
            if len(filtered_df) > 0:
                license_counts = filtered_df['license'].value_counts().head(8)
                
                fig, ax = plt.subplots(figsize=(8, 4))
                ax.bar(range(len(license_counts)), license_counts.values,
                      color='orange', alpha=0.7)
                ax.set_xticks(range(len(license_counts)))
                ax.set_xticklabels(license_counts.index, rotation=45, ha='right')
                ax.set_ylabel('Number of Publications')
                ax.set_title('Publications by License Type')
                ax.grid(True, alpha=0.3)
                
                st.pyplot(fig)
    
    with tab4:
        st.subheader("Data Quality Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Missing Data Overview**")
            important_cols = ['title', 'abstract', 'authors', 'journal']
            missing_data = filtered_df[important_cols].apply(
                lambda x: (x == 'No abstract available') | (x == 'Unknown authors') | (x == 'Unknown journal')
            ).sum()
            
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.bar(missing_data.index, missing_data.values, color='red', alpha=0.7)
            ax.set_ylabel('Count of Missing/Imputed Values')
            ax.set_title('Data Completeness Issues')
            plt.xticks(rotation=45)
            st.pyplot(fig)
        
        with col2:
            st.write("**Abstract Availability**")
            if len(filtered_df) > 0:
                abstract_stats = filtered_df['has_abstract'].value_counts()
                
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.pie(abstract_stats.values, labels=['With Abstract', 'Without Abstract'],
                      autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
                ax.set_title('Abstract Availability')
                st.pyplot(fig)
    
    # Data sample section
    st.header("📋 Data Sample")
    
    sample_size = st.slider("Select sample size", 5, 50, 10)
    
    display_columns = ['title', 'authors', 'journal', 'publication_year', 'source_x']
    sample_data = filtered_df[display_columns].head(sample_size)
    
    # Format for better display
    sample_data_display = sample_data.copy()
    sample_data_display['title'] = sample_data_display['title'].apply(
        lambda x: x[:70] + '...' if len(str(x)) > 70 else x
    )
    sample_data_display['authors'] = sample_data_display['authors'].apply(
        lambda x: x[:40] + '...' if len(str(x)) > 40 else x
    )
    
    st.dataframe(sample_data_display, use_container_width=True)
    
    # Download functionality
    st.subheader("📥 Download Data")
    csv_data = filtered_df[display_columns].to_csv(index=False)
    st.download_button(
        label="Download filtered data as CSV",
        data=csv_data,
        file_name="cord19_filtered_data.csv",
        mime="text/csv"
    )
    
    # Search functionality
    st.header("🔍 Search Papers")
    search_query = st.text_input("Search in titles and abstracts:")
    
    if search_query:
        search_results = filtered_df[
            filtered_df['title'].str.contains(search_query, case=False, na=False) |
            filtered_df['abstract'].str.contains(search_query, case=False, na=False)
        ]
        
        st.write(f"Found {len(search_results)} papers matching '{search_query}'")
        
        if len(search_results) > 0:
            st.dataframe(search_results[display_columns].head(20), use_container_width=True)

else:
    st.error("Failed to load data. Please ensure the cleaned dataset exists.")