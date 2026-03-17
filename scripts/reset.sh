#!/bin/bash
echo "Deleting all agents..."
orchestrate agents delete orchestrator
orchestrate agents delete research-agent
echo "Reset complete."
