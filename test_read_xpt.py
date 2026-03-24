"""Tests for read_xpt module."""

import os
import tempfile

import pandas as pd
import pyreadstat

from read_xpt import read_xpt


def _create_temp_xpt(data: dict, path: str) -> None:
    """Write a temporary XPT file for testing."""
    df = pd.DataFrame(data)
    pyreadstat.write_xport(df, path, file_format_version=5)


def test_read_xpt_returns_dataframe():
    data = {"A": [1, 2], "B": [3.0, 4.0]}
    with tempfile.NamedTemporaryFile(suffix=".xpt", delete=False) as f:
        tmp_path = f.name
    try:
        _create_temp_xpt(data, tmp_path)
        result = read_xpt(tmp_path)
        assert isinstance(result, pd.DataFrame)
        assert list(result.columns) == ["A", "B"]
        assert len(result) == 2
    finally:
        os.unlink(tmp_path)


def test_read_xpt_values():
    data = {"X": [10], "Y": ["hello"]}
    with tempfile.NamedTemporaryFile(suffix=".xpt", delete=False) as f:
        tmp_path = f.name
    try:
        _create_temp_xpt(data, tmp_path)
        result = read_xpt(tmp_path)
        assert result["X"].iloc[0] == 10.0
        assert result["Y"].iloc[0] == "hello"
    finally:
        os.unlink(tmp_path)


def test_read_data_xpt():
    """Test reading the sample data.xpt shipped with the repo."""
    repo_xpt = os.path.join(os.path.dirname(__file__), "data.xpt")
    if not os.path.exists(repo_xpt):
        return  # skip if file not present
    result = read_xpt(repo_xpt)
    assert len(result) == 5
    assert "ID" in result.columns
    assert "NAME" in result.columns
    assert "AGE" in result.columns
    assert "SCORE" in result.columns
