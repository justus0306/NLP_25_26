#!/usr/bin/env python3
"""
Script to merge multi-label and single-label datasets into unified parquet files.
This creates the consolidated dataset structure with all columns in one file.
"""

import pandas as pd
import numpy as np
from pathlib import Path

def create_single_label_binary_vector(single_label_name, label_name_list):
    """
    Create a binary vector for single label based on the position in label_name_list.
    
    Args:
        single_label_name: String, the single label name (e.g., "sports")
        label_name_list: List of possible labels in order
        
    Returns:
        String representation of binary vector (e.g., "[0 0 0 0 0 1]")
    """
    # Parse label_name_list if it's a string representation
    if isinstance(label_name_list, str):
        # Extract labels from string like "['sports']"
        import ast
        try:
            label_name_list = ast.literal_eval(label_name_list)
        except:
            label_name_list = []
    
    # Create binary vector with 1 at the position of the single label
    vector = [0] * 6  # We know there are 6 labels after filtering
    
    # Mapping of label names to indices (based on the filtered label order)
    label_to_idx = {
        'sports': 5,
        'news_&_social_concern': 3,
        'film_tv_&_video': 2,
        'gaming': 4,
        'music': 1,
        'food_&_dining': 0
    }
    
    if single_label_name in label_to_idx:
        vector[label_to_idx[single_label_name]] = 1
    
    # Return as string format matching the existing format
    return '[' + ' '.join(map(str, vector)) + ']'


def merge_datasets(split_name):
    """
    Merge multi-label and single-label datasets for a given split.
    
    Args:
        split_name: One of 'train', 'test', or 'validation'
    """
    print(f"\nProcessing {split_name} split...")
    
    # Load multi-label data
    ml_path = f'Abgabe/Data/multi_label/tweets_preprocessed_{split_name}.parquet'
    ml_df = pd.read_parquet(ml_path)
    print(f"  Loaded multi-label: {len(ml_df)} rows")
    
    # Load single-label data
    sl_path = f'Abgabe/Data/single_label/tweets_single_label_{split_name}.parquet'
    sl_df = pd.read_parquet(sl_path)
    print(f"  Loaded single-label: {len(sl_df)} rows")
    
    # Verify that the datasets match
    assert len(ml_df) == len(sl_df), f"Row count mismatch for {split_name}"
    assert (ml_df['id'].values == sl_df['id'].values).all(), f"ID mismatch for {split_name}"
    
    # Note: text_original would ideally be the text before preprocessing (after number removal)
    # Since we don't have it saved, we'll use the preprocessed text as a placeholder
    # The lab2.ipynb notebook will be updated to save text_original properly going forward
    
    # Create the unified dataset with correct column order:
    # 1. text - preprocessed tweet text
    # 2. text_original - original tweet text (placeholder: using preprocessed text until notebook is re-run)
    # 3. label - multi-label binary vector
    # 4. label_name - multi-label names list
    # 5. single_label - single-label binary vector
    # 6. single_label_name - single label name string
    # 7. id - tweet id
    
    unified_df = pd.DataFrame()
    unified_df['text'] = ml_df['text']
    unified_df['text_original'] = ml_df['text']  # Placeholder: will be properly populated when notebook is re-run
    unified_df['label'] = ml_df['label']
    unified_df['label_name'] = ml_df['label_name']
    
    # Create single_label binary vector
    unified_df['single_label'] = sl_df.apply(
        lambda row: create_single_label_binary_vector(row['single_label'], row['label_name']),
        axis=1
    )
    unified_df['single_label_name'] = sl_df['single_label']
    unified_df['id'] = ml_df['id']
    
    # Save the unified dataset
    output_path = f'Abgabe/Data/tweets_preprocessed_{split_name}.parquet'
    unified_df.to_parquet(output_path, index=False)
    print(f"  Saved unified dataset: {output_path}")
    print(f"  Columns: {list(unified_df.columns)}")
    print(f"  Shape: {unified_df.shape}")
    
    # Show a sample
    print(f"\n  Sample row:")
    print(f"    text: {unified_df['text'].iloc[0][:60]}...")
    print(f"    text_original: {unified_df['text_original'].iloc[0][:60]}...")
    print(f"    label: {unified_df['label'].iloc[0]}")
    print(f"    label_name: {unified_df['label_name'].iloc[0]}")
    print(f"    single_label: {unified_df['single_label'].iloc[0]}")
    print(f"    single_label_name: {unified_df['single_label_name'].iloc[0]}")
    print(f"    id: {unified_df['id'].iloc[0]}")


def main():
    print("="*80)
    print("MERGING MULTI-LABEL AND SINGLE-LABEL DATASETS")
    print("="*80)
    
    # Process all splits
    for split in ['train', 'test', 'validation']:
        merge_datasets(split)
    
    print("\n" + "="*80)
    print("✓ All datasets merged successfully!")
    print("="*80)
    print("\nOutput files:")
    print("  - Abgabe/Data/tweets_preprocessed_train.parquet")
    print("  - Abgabe/Data/tweets_preprocessed_test.parquet")
    print("  - Abgabe/Data/tweets_preprocessed_validation.parquet")


if __name__ == '__main__':
    main()
