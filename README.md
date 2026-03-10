# AI-Ops DevOps Platform (LangChain)

An AI-powered DevOps platform that combines Kubernetes observability,
rule-based remediation, and LangChain-driven AI agents to detect,
analyze, and resolve infrastructure and application incidents.

This project demonstrates how AI can assist SRE and DevOps teams
with incident detection, root cause analysis, and automated remediation.

The goal is to evolve traditional DevOps automation into **AI-driven
DevOps (AI-Ops)**.
------------------------------------------------------------------------
## Architecture Overview

The system combines observability tools with AI reasoning agents.

Kubernetes Cluster
      │
      ▼
Prometheus + Elasticsearch
      │
      ▼
Rule Engine
      │
 ┌────┴─────────┐
 │              │
 ▼              ▼
Known Issues   Unknown Issues
Auto Fix       LangChain Analysis


![Architecture Diagram](gitops/images/Full_architecture.png)

------------------------------------------------------------------------

## Repository Structure

AI-Ops-DevOps-Platform-Langchain
│
├── app
│ ├── backend
│ └── frontend
│
├── infra
│
├── gitops
│ └── infra-apps
│
├── ai-ops
│ ├── agent
│ ├── collectors
│ ├── remediation
│ ├── knowledge
│ ├── config
│ └── ai
│
└── monitoring
------------------------------------------------------------------------

# AI Agents in the System

## Monitoring Agent

Responsibilities:

-   Collect metrics from Prometheus
-   Collect logs from Elasticsearch
-   Monitor Kubernetes cluster state
-   Detect anomalies

Inputs:

-   Node metrics
-   Container metrics
-   Application logs
-   Kubernetes events

Outputs:

-   Incident detection signals

------------------------------------------------------------------------
## Features

- Kubernetes monitoring using Prometheus
- Centralized logging with ELK Stack
- Rule-based incident detection
- Automated remediation (restart pods, scale deployments, cleanup logs)
- Security anomaly detection
- AI-powered incident analysis using LangChain
- Modular AI agent architecture

------------------------------------------------------------------------

## Incident Analysis Agent

This agent performs **AI-powered root cause analysis**.

Responsibilities:

-   Analyze logs and metrics
-   Correlate events across systems
-   Identify root cause
-   Suggest remediation

Example:

    Root Cause: Database connection pool exhausted

    Suggested Fix:
    1. Restart API deployment
    2. Investigate database latency

------------------------------------------------------------------------

## Remediation Agent

Performs automated recovery actions.

Safe automated actions:

-   Restart failed pods
-   Restart deployments
-   Scale deployments
-   Cleanup logs
-   Restart DNS services

------------------------------------------------------------------------

## Security Agent

Detects and responds to attacks.

Capabilities:

-   Detect brute force login attempts
-   Detect suspicious API traffic
-   Detect SQL injection patterns
-   Detect abnormal request spikes

Response actions:

-   Block malicious IPs
-   Generate security alerts
-   Notify engineers

------------------------------------------------------------------------

# AI-Ops Workflow

    Cluster Monitoring
            |
            v
    Incident Detection
            |
            v
    Rule Engine
            |
      +-----+------
      |           |
      v           v
    Known Issue   Unknown Issue
    Auto Fix      AI Analysis
            |
            v
    Incident Resolved

------------------------------------------------------------------------

# Project Directory Structure

    AI-Assisted-DevOps-Project
    |
    |-- app
    |   |-- backend
    |   |-- frontend
    |
    |-- infra
    |
    |-- gitops
    |   |-- infra-apps
    |
    |-- ai-ops
    |   |-- agent
    |   |-- collectors
    |   |-- remediation
    |   |-- knowledge
    |   |-- config
    |   |-- llm
    |
    |-- monitoring

------------------------------------------------------------------------

# Technologies Used

Infrastructure - Kubernetes - Docker - Terraform

Observability - Prometheus - Elasticsearch - Kibana

AI / Automation - Python - AI Agents - Rule Engine - LLM Integration
(ChatGPT / Claude)

------------------------------------------------------------------------

## Future Roadmap

- LangChain-based incident analysis agent
- AI-assisted runbook generation
- ChatOps interface for Kubernetes
- Security threat detection
- Multi-agent AI-Ops architecture
