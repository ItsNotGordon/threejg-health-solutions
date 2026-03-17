#!/bin/bash
set -e

echo "Activating environment..."
orchestrate env activate hackathon

echo "Importing tools..."
orchestrate tools import -f tools/search.py

echo "Importing agents..."
orchestrate agents import -f agents/orchestrator.yaml
orchestrate agents import -f agents/research.yaml

echo "Done. All agents deployed."
