# -*- coding: utf-8 -*-
"""
Builder to generate index.html with Home + Lever + Pulley + Incline
"""
import os

def generate():
    print("Writing index.html...")
    with open("index.html", "w", encoding="utf-8") as f:
        # We will write the file in clear modular sections
        write_header_and_styles(f)
        write_home_view(f)
        write_lever_view(f)
        write_pulley_view(f)
        write_incline_view(f)
        write_javascript(f)
    print("Successfully generated index.html!")

def write_header_and_styles(f):
    f.write('''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>STEM Lab: เครื่องกลอย่างง่าย ม.1 (Simple Machines Lab)</title>
  
  <!-- Google Fonts: Prompt & Noto Sans Thai -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@400;500;600;700&family=Prompt:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --primary-light: #dbeafe;
      --accent: #f59e0b;
      --accent-dark: #d97706;
      --success: #10b981;
      --success-light: #d1fae5;
      --danger: #ef4444;
      --danger-light: #fee2e2;
      --purple: #8b5cf6;
      --purple-light: #ede9fe;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
      --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
      --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
      --radius-full: 9999px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }

    body {
      font-family: 'Noto Sans Thai', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.6;
      font-size: 16px;
      overflow-x: hidden;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    h1, h2, h3, h4, .font-prompt {
      font-family: 'Prompt', sans-serif;
      font-weight: 700;
    }

    header {
      background: #ffffff;
      border-bottom: 2px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: var(--shadow-sm);
    }

    .header-container {
      max-width: 1240px;
      margin: 0 auto;
      padding: 0.75rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .logo-area { display: flex; align-items: center; gap: 0.75rem; cursor: pointer; }
    .logo-icon {
      width: 44px; height: 44px;
      background: linear-gradient(135deg, var(--primary), var(--purple));
      color: white; border-radius: var(--radius-md);
      display: flex; align-items: center; justify-content: center;
      font-size: 1.5rem; box-shadow: 0 4px 10px rgba(37,99,235,0.3);
    }
    .logo-text h1 { font-size: 1.2rem; color: var(--text-main); line-height: 1.2; }
    .logo-text span { font-size: 0.8rem; color: var(--text-muted); font-weight: 500; }

    .header-actions { display: flex; align-items: center; gap: 0.75rem; }

    .star-badge {
      display: flex; align-items: center; gap: 0.4rem;
      background: #fffbeb; border: 2px solid #fde68a;
      padding: 0.4rem 0.85rem; border-radius: var(--radius-full);
      font-family: 'Prompt', sans-serif; font-weight: 700;
      color: var(--accent-dark); font-size: 1rem;
      box-shadow: var(--shadow-sm);
    }
    .star-badge span.star-icon {
      font-size: 1.2rem; color: var(--accent);
      filter: drop-shadow(0 1px 2px rgba(245,158,11,0.5));
    }

    .btn-icon {
      min-width: 44px; min-height: 44px;
      border: 2px solid var(--border); background: #ffffff;
      border-radius: var(--radius-md);
      display: inline-flex; align-items: center; justify-content: center;
      font-size: 1.2rem; cursor: pointer; color: var(--text-main);
      transition: all 0.2s;
    }
    .btn-icon:hover { background: var(--primary-light); border-color: var(--primary); color: var(--primary); }

    .btn-nav-home {
      display: flex; align-items: center; gap: 0.4rem;
      padding: 0.45rem 0.9rem; border-radius: var(--radius-md);
      background: var(--primary-light); color: var(--primary-dark);
      border: 1px solid #bfdbfe; font-family: 'Prompt', sans-serif;
      font-weight: 600; font-size: 0.95rem; cursor: pointer;
      min-height: 44px; transition: all 0.2s;
    }
    .btn-nav-home:hover { background: var(--primary); color: #ffffff; }

    main {
      flex: 1; max-width: 1240px; width: 100%;
      margin: 0 auto; padding: 1.25rem;
    }

    .view-section { display: none; animation: fadeIn 0.3s ease; }
    .view-section.active { display: block; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

    /* Hero Banner */
    .hero-banner {
      background: linear-gradient(135deg, #eff6ff 0%, #e0e7ff 100%);
      border: 2px solid #bfdbfe; border-radius: var(--radius-lg);
      padding: 1.75rem 2rem; margin-bottom: 2rem;
      position: relative; overflow: hidden; box-shadow: var(--shadow-sm);
    }
    .hero-content { display: flex; align-items: center; gap: 1.5rem; }
    .mascot-avatar {
      width: 80px; height: 80px; background: #ffffff;
      border-radius: var(--radius-full); display: flex; align-items: center; justify-content: center;
      font-size: 3rem; box-shadow: var(--shadow-md); border: 3px solid var(--primary);
      flex-shrink: 0; animation: floatMascot 3s ease-in-out infinite;
    }
    @keyframes floatMascot { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
    .hero-text h2 { font-size: 1.75rem; color: #1e3a8a; margin-bottom: 0.3rem; }
    .hero-text p { font-size: 1.05rem; color: #334155; max-width: 800px; }
    .hero-rule-pill {
      display: inline-block; margin-top: 0.6rem;
      background: #ffffff; color: #1d4ed8; font-weight: 700;
      padding: 0.35rem 1rem; border-radius: var(--radius-full);
      font-size: 0.95rem; border: 1.5px solid #93c5fd;
    }

    /* Grid of Machines */
    .machines-grid {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.5rem; margin-bottom: 2rem;
    }
    .machine-card {
      background: var(--card-bg); border-radius: var(--radius-lg);
      border: 2px solid var(--border); padding: 1.5rem;
      box-shadow: var(--shadow-sm); display: flex; flex-direction: column;
      justify-content: space-between; transition: all 0.25s ease;
      position: relative;
    }
    .machine-card:hover:not(.locked) { transform: translateY(-4px); box-shadow: var(--shadow-lg); border-color: var(--primary); }
    .machine-card.active-card { border-color: #93c5fd; background: linear-gradient(to bottom, #ffffff, #f8faff); }
    .machine-card.locked { opacity: 0.75; background: #fafafa; border-style: dashed; }
    .card-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem; }
    .card-icon-box {
      width: 56px; height: 56px; border-radius: var(--radius-md);
      display: flex; align-items: center; justify-content: center; font-size: 2rem;
    }
    .card-stars-earned {
      display: flex; align-items: center; gap: 0.25rem;
      background: #fffbeb; padding: 0.3rem 0.6rem; border-radius: var(--radius-full);
      font-family: 'Prompt', sans-serif; font-weight: 700; font-size: 0.9rem;
      color: var(--accent-dark); border: 1px solid #fef3c7;
    }
    .card-title { font-size: 1.35rem; color: var(--text-main); margin-bottom: 0.4rem; }
    .card-subtitle { font-size: 0.95rem; color: var(--text-muted); margin-bottom: 1rem; min-height: 48px; }
    .card-formula-tag {
      background: #f1f5f9; color: #475569; font-size: 0.85rem;
      padding: 0.35rem 0.65rem; border-radius: var(--radius-sm);
      display: inline-block; margin-bottom: 1.25rem; font-family: monospace; font-weight: 600;
    }
    .btn-enter-room {
      width: 100%; min-height: 48px; background: var(--primary); color: white;
      border: none; border-radius: var(--radius-md); font-family: 'Prompt', sans-serif;
      font-size: 1.05rem; font-weight: 600; cursor: pointer;
      display: flex; align-items: center; justify-content: center; gap: 0.5rem; transition: background 0.2s;
    }
    .btn-enter-room:hover { background: var(--primary-dark); }
    .badge-locked {
      background: #e2e8f0; color: #64748b; font-size: 0.85rem;
      padding: 0.5rem 1rem; border-radius: var(--radius-md);
      text-align: center; font-weight: 600;
    }

    /* Overall Summary Card */
    .summary-card {
      background: #ffffff; border: 2px solid var(--border); border-radius: var(--radius-lg);
      padding: 1.5rem; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 1.5rem;
    }
    .summary-info h3 { font-size: 1.2rem; margin-bottom: 0.2rem; }
    .summary-info p { color: var(--text-muted); font-size: 0.95rem; }

    /* Room Header & Tabs */
    .room-header {
      background: #ffffff; border: 2px solid var(--border); border-radius: var(--radius-lg);
      padding: 1.25rem 1.5rem; margin-bottom: 1.25rem; display: flex; flex-wrap: wrap;
      justify-content: space-between; align-items: center; gap: 1rem; box-shadow: var(--shadow-sm);
    }
    .room-title-area { display: flex; align-items: center; gap: 0.75rem; }
    .room-title-area .room-icon { font-size: 2.2rem; }
    .room-title-area h2 { font-size: 1.5rem; color: var(--text-main); }
    .room-title-area p { color: var(--text-muted); font-size: 0.92rem; }

    .room-tabs {
      display: flex; flex-wrap: wrap; gap: 0.5rem;
      background: #f1f5f9; padding: 0.35rem; border-radius: var(--radius-md);
    }
    .tab-btn {
      min-height: 44px; padding: 0.4rem 1rem; border: none; background: transparent;
      border-radius: var(--radius-sm); font-family: 'Prompt', sans-serif;
      font-size: 0.95rem; font-weight: 600; color: var(--text-muted); cursor: pointer;
      display: flex; align-items: center; gap: 0.4rem; transition: all 0.2s;
    }
    .tab-btn.active { background: #ffffff; color: var(--primary); box-shadow: var(--shadow-sm); }
    .tab-btn:hover:not(.active) { color: var(--text-main); }

    .tab-content-panel { display: none; animation: fadeIn 0.25s ease; }
    .tab-content-panel.active { display: block; }

    /* Simulation Layout Grid */
    .sim-layout {
      display: grid; grid-template-columns: 1fr 340px; gap: 1.25rem; margin-bottom: 1.5rem;
    }
    @media (max-width: 980px) { .sim-layout { grid-template-columns: 1fr; } }

    .sim-stage-card {
      background: #ffffff; border: 2px solid var(--border); border-radius: var(--radius-lg);
      padding: 1.25rem; box-shadow: var(--shadow-sm); display: flex; flex-direction: column; position: relative;
    }
    .stage-status-bar {
      display: flex; justify-content: space-between; align-items: center;
      margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem;
    }
    .balance-status-badge {
      display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.4rem 0.9rem;
      border-radius: var(--radius-full); font-family: 'Prompt', sans-serif; font-weight: 700;
      font-size: 0.95rem; transition: all 0.3s;
    }
    .balance-status-badge.balanced { background: var(--success-light); color: #065f46; border: 1.5px solid #a7f3d0; }
    .balance-status-badge.tilted-left { background: #eff6ff; color: #1e40af; border: 1.5px solid #bfdbfe; }
    .balance-status-badge.tilted-right { background: #fffbeb; color: #b45309; border: 1.5px solid #fde68a; }

    .hint-drag-tag {
      font-size: 0.85rem; color: var(--text-muted); background: #f8fafc;
      border: 1px solid var(--border); padding: 0.25rem 0.6rem; border-radius: var(--radius-sm);
      display: flex; align-items: center; gap: 0.3rem;
    }

    .svg-container {
      width: 100%; height: 380px;
      background: radial-gradient(circle at 50% 30%, #ffffff 0%, #f1f5f9 100%);
      border-radius: var(--radius-md); border: 2px solid #e2e8f0;
      position: relative; touch-action: none; user-select: none;
    }
    svg.sim-svg { width: 100%; height: 100%; overflow: visible; }

    .stage-quick-actions {
      display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.85rem; align-items: center;
    }
    .btn-quick {
      min-height: 44px; padding: 0.4rem 0.85rem; background: #f1f5f9;
      border: 1px solid var(--border); border-radius: var(--radius-md);
      font-size: 0.88rem; font-weight: 600; color: #334155; cursor: pointer;
      display: inline-flex; align-items: center; gap: 0.35rem; transition: all 0.2s;
    }
    .btn-quick:hover { background: var(--primary-light); border-color: #93c5fd; color: var(--primary-dark); }
    .btn-simulate-action {
      min-height: 44px; padding: 0.4rem 1.25rem;
      background: linear-gradient(135deg, var(--accent), var(--accent-dark));
      color: white; border: none; border-radius: var(--radius-md);
      font-family: 'Prompt', sans-serif; font-weight: 700; font-size: 0.95rem;
      cursor: pointer; display: inline-flex; align-items: center; gap: 0.5rem;
      box-shadow: 0 2px 4px rgba(245,158,11,0.3); margin-left: auto; transition: all 0.2s;
    }
    .btn-simulate-action:hover { filter: brightness(1.08); transform: translateY(-1px); }

    /* Side Controls Panel */
    .side-controls-panel { display: flex; flex-direction: column; gap: 1rem; }
    .control-group-card {
      background: #ffffff; border: 2px solid var(--border); border-radius: var(--radius-md);
      padding: 1rem; box-shadow: var(--shadow-sm);
    }
    .control-group-title {
      font-size: 0.95rem; color: var(--text-muted); margin-bottom: 0.65rem;
      display: flex; align-items: center; justify-content: space-between;
    }
    .slider-row { margin-bottom: 0.85rem; }
    .slider-row:last-child { margin-bottom: 0; }
    .slider-label-row {
      display: flex; justify-content: space-between; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.25rem;
    }
    .slider-val-tag { font-family: 'Prompt', sans-serif; color: var(--primary); font-weight: 700; }

    input[type=range] {
      width: 100%; height: 8px; border-radius: 4px; background: #e2e8f0;
      outline: none; -webkit-appearance: none; cursor: pointer;
    }
    input[type=range]::-webkit-slider-thumb {
      -webkit-appearance: none; width: 24px; height: 24px; border-radius: 50%;
      background: var(--primary); border: 2px solid #ffffff;
      box-shadow: 0 2px 6px rgba(0,0,0,0.25); cursor: pointer; transition: transform 0.1s;
    }
    input[type=range]::-webkit-slider-thumb:hover { transform: scale(1.15); }

    .stepper-box { display: flex; align-items: center; gap: 0.4rem; margin-top: 0.35rem; }
    .btn-step {
      min-width: 44px; min-height: 38px; background: #f1f5f9; border: 1px solid var(--border);
      border-radius: var(--radius-sm); font-size: 1.1rem; font-weight: 700; color: var(--text-main);
      cursor: pointer; display: inline-flex; align-items: center; justify-content: center;
    }
    .btn-step:hover { background: #e2e8f0; }

    /* Metrics Dashboard */
    .metrics-grid {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1rem; margin-bottom: 1.5rem;
    }
    .metric-card {
      background: #ffffff; border: 2px solid var(--border); border-radius: var(--radius-md);
      padding: 1rem 1.25rem; box-shadow: var(--shadow-sm); display: flex; align-items: center; gap: 1rem;
    }
    .metric-icon-box {
      width: 48px; height: 48px; border-radius: var(--radius-md);
      display: flex; align-items: center; justify-content: center; font-size: 1.5rem; flex-shrink: 0;
    }
    .metric-info h4 { font-size: 0.85rem; color: var(--text-muted); font-weight: 600; }
    .metric-value {
      font-size: 1.45rem; font-family: 'Prompt', sans-serif; font-weight: 800; color: var(--text-main); line-height: 1.2;
    }
    .metric-desc { font-size: 0.78rem; color: var(--text-muted); }

    /* Work conservation banner */
    .work-conservation-card {
      background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
      border: 2px solid #a7f3d0; border-radius: var(--radius-lg);
      padding: 1.25rem 1.5rem; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 1.25rem;
    }
    .work-icon { font-size: 2.2rem; color: #059669; }
    .work-text h4 { color: #065f46; font-size: 1.1rem; margin-bottom: 0.25rem; }
    .work-text p { color: #047857; font-size: 0.95rem; }

    /* Knowledge Box */
    .knowledge-box {
      background: #ffffff; border: 2px solid var(--border); border-radius: var(--radius-lg);
      padding: 1.5rem; margin-bottom: 1.5rem;
    }
    .knowledge-title {
      font-size: 1.25rem; color: #1e3a8a; display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;
    }
    .knowledge-grid {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem;
    }
    .knowledge-item {
      background: #f8fafc; border-radius: var(--radius-md); padding: 1rem; border-left: 4px solid var(--primary);
    }
    .knowledge-item h5 { font-size: 1rem; color: var(--text-main); margin-bottom: 0.35rem; }
    .knowledge-item p { font-size: 0.9rem; color: #475569; }

    /* Predict Mode Box */
    .predict-box {
      background: #ffffff; border: 2px solid var(--border); border-radius: var(--radius-lg);
      padding: 1.75rem; box-shadow: var(--shadow-sm);
    }
    .predict-header { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.25rem; }
    .predict-header .predict-icon { font-size: 2rem; }
    .predict-scenario-card {
      background: #eff6ff; border: 1.5px solid #bfdbfe; border-radius: var(--radius-md);
      padding: 1.25rem; margin-bottom: 1.25rem;
    }
    .predict-options-list { display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 1.5rem; }
    .predict-option-btn {
      min-height: 50px; padding: 0.75rem 1.25rem; background: #ffffff;
      border: 2px solid var(--border); border-radius: var(--radius-md);
      font-family: 'Noto Sans Thai', sans-serif; font-size: 1rem; font-weight: 500;
      color: var(--text-main); cursor: pointer; text-align: left;
      display: flex; align-items: center; gap: 0.75rem; transition: all 0.2s;
    }
    .predict-option-btn:hover { border-color: var(--primary); background: #f8faff; }
    .predict-option-btn.selected {
      border-color: var(--primary); background: var(--primary-light); color: var(--primary-dark); font-weight: 700;
    }
    .predict-option-btn .opt-badge {
      min-width: 32px; min-height: 32px; border-radius: 50%; background: #e2e8f0;
      display: flex; align-items: center; justify-content: center; font-weight: 700;
    }
    .predict-option-btn.selected .opt-badge { background: var(--primary); color: white; }

    .btn-run-prediction {
      min-height: 48px; padding: 0.6rem 1.75rem; background: var(--primary);
      color: white; border: none; border-radius: var(--radius-md);
      font-family: 'Prompt', sans-serif; font-size: 1.05rem; font-weight: 700;
      cursor: pointer; display: inline-flex; align-items: center; gap: 0.5rem; transition: background 0.2s;
    }
    .btn-run-prediction:disabled { background: #cbd5e1; cursor: not-allowed; }
    .predict-result-box {
      margin-top: 1.5rem; padding: 1.25rem; border-radius: var(--radius-md); display: none; animation: fadeIn 0.3s ease;
    }
    .predict-result-box.correct { background: #d1fae5; border: 2px solid #34d399; color: #065f46; }
    .predict-result-box.incorrect { background: #fee2e2; border: 2px solid #f87171; color: #991b1b; }

    /* Missions Mode */
    .missions-container { display: flex; flex-direction: column; gap: 1.25rem; }
    .mission-card {
      background: #ffffff; border: 2px solid var(--border); border-radius: var(--radius-lg);
      padding: 1.5rem; box-shadow: var(--shadow-sm); position: relative; transition: all 0.2s;
    }
    .mission-card.completed { border-color: #34d399; background: linear-gradient(to right, #ffffff, #f0fdf4); }
    .mission-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem; }
    .mission-num-badge {
      display: inline-flex; align-items: center; gap: 0.4rem; background: #f1f5f9;
      padding: 0.3rem 0.75rem; border-radius: var(--radius-full);
      font-family: 'Prompt', sans-serif; font-weight: 700; font-size: 0.85rem; color: #475569;
    }
    .mission-card.completed .mission-num-badge { background: #d1fae5; color: #065f46; }
    .mission-star-award { font-size: 1.25rem; color: #cbd5e1; }
    .mission-card.completed .mission-star-award { color: var(--accent); filter: drop-shadow(0 2px 4px rgba(245,158,11,0.4)); }
    .mission-title { font-size: 1.25rem; color: var(--text-main); margin-bottom: 0.4rem; }
    .mission-desc { color: #475569; font-size: 0.98rem; margin-bottom: 1.25rem; }
    .mission-actions { display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center; }
    .btn-apply-mission {
      min-height: 44px; padding: 0.4rem 1.25rem; background: var(--primary);
      color: white; border: none; border-radius: var(--radius-md); font-family: 'Prompt', sans-serif;
      font-weight: 600; font-size: 0.95rem; cursor: pointer; display: inline-flex; align-items: center; gap: 0.4rem;
    }
    .btn-check-mission {
      min-height: 44px; padding: 0.4rem 1.25rem; background: var(--success);
      color: white; border: none; border-radius: var(--radius-md); font-family: 'Prompt', sans-serif;
      font-weight: 700; font-size: 0.95rem; cursor: pointer; display: inline-flex; align-items: center; gap: 0.4rem;
    }
    .mission-feedback { margin-top: 0.75rem; font-size: 0.95rem; font-weight: 600; display: none; }

    /* Quiz Mode */
    .quiz-container {
      background: #ffffff; border: 2px solid var(--border); border-radius: var(--radius-lg);
      padding: 1.75rem; box-shadow: var(--shadow-sm);
    }
    .quiz-question-item { padding-bottom: 1.5rem; margin-bottom: 1.5rem; border-bottom: 1px solid var(--border); }
    .quiz-question-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
    .quiz-q-title { font-size: 1.15rem; color: var(--text-main); margin-bottom: 1rem; display: flex; gap: 0.5rem; }
    .quiz-choices { display: flex; flex-direction: column; gap: 0.6rem; }
    .quiz-choice-label {
      display: flex; align-items: center; gap: 0.75rem; padding: 0.75rem 1rem;
      border: 1.5px solid var(--border); border-radius: var(--radius-md); cursor: pointer;
      transition: all 0.2s; font-size: 0.95rem;
    }
    .quiz-choice-label:hover { background: #f8fafc; border-color: #cbd5e1; }
    .quiz-choice-label.correct-answer { background: #d1fae5; border-color: #34d399; color: #065f46; font-weight: 600; }
    .quiz-choice-label.wrong-answer { background: #fee2e2; border-color: #f87171; color: #991b1b; }
    .quiz-choice-label input[type="radio"] { width: 20px; height: 20px; accent-color: var(--primary); }
    .quiz-explanation {
      margin-top: 0.6rem; padding: 0.75rem 1rem; background: #f8fafc;
      border-left: 3px solid var(--primary); border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      font-size: 0.9rem; color: #334155; display: none;
    }
    .quiz-footer {
      display: flex; justify-content: space-between; align-items: center;
      margin-top: 1.5rem; padding-top: 1.25rem; border-top: 2px solid var(--border); flex-wrap: wrap; gap: 1rem;
    }
    .quiz-score-badge { font-family: 'Prompt', sans-serif; font-weight: 700; font-size: 1.1rem; color: var(--primary-dark); }

    /* Toast */
    .celebration-toast {
      position: fixed; bottom: 24px; right: 24px; background: #1e293b; color: white;
      padding: 1rem 1.5rem; border-radius: var(--radius-lg); box-shadow: var(--shadow-lg);
      display: flex; align-items: center; gap: 0.75rem; z-index: 2000;
      transform: translateY(100px); opacity: 0; transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .celebration-toast.show { transform: translateY(0); opacity: 1; }

    /* Segment Buttons (Selector pills) */
    .pill-selector { display: flex; gap: 0.4rem; background: #f1f5f9; padding: 0.3rem; border-radius: var(--radius-md); }
    .pill-btn {
      flex: 1; min-height: 40px; border: none; background: transparent; border-radius: var(--radius-sm);
      font-family: 'Prompt', sans-serif; font-size: 0.9rem; font-weight: 600; color: #64748b; cursor: pointer;
      display: inline-flex; align-items: center; justify-content: center; gap: 0.3rem; transition: all 0.2s;
    }
    .pill-btn.active { background: #ffffff; color: var(--primary); box-shadow: var(--shadow-sm); }

    @media (max-width: 768px) {
      body { font-size: 15px; }
      .header-container { padding: 0.5rem 1rem; }
      .logo-text span { display: none; }
      .hero-content { flex-direction: column; text-align: center; }
      .hero-text h2 { font-size: 1.4rem; }
      .svg-container { height: 320px; }
      .room-header { flex-direction: column; align-items: flex-start; }
      .room-tabs { width: 100%; overflow-x: auto; }
      .tab-btn { flex: 1; justify-content: center; white-space: nowrap; }
    }
  </style>
</head>
<body>

  <!-- TOP HEADER -->
  <header>
    <div class="header-container">
      <div class="logo-area" onclick="App.navigateHome()" title="กลับหน้าแรก">
        <div class="logo-icon">⚙️</div>
        <div class="logo-text">
          <h1>STEM เครื่องกลอย่างง่าย</h1>
          <span>ห้องเรียนวิทยาศาสตร์ ม.1</span>
        </div>
      </div>

      <div class="header-actions">
        <button id="btn-back-home" class="btn-nav-home" onclick="App.navigateHome()" style="display: none;">
          🏠 <span>หน้าแรก</span>
        </button>

        <div class="star-badge" title="ดาวความสำเร็จสะสม">
          <span class="star-icon">⭐</span>
          <span id="global-star-count">0</span> / 20
        </div>

        <button id="btn-sound-toggle" class="btn-icon" onclick="Sound.toggle()" title="เปิด/ปิดเสียงเอฟเฟกต์">
          🔊
        </button>
      </div>
    </div>
  </header>

  <main>
''')

def write_home_view(f):
    f.write('''
    <!-- ========================================================================
         VIEW 1: HOME VIEW
         ======================================================================== -->
    <section id="view-home" class="view-section active">
      
      <div class="hero-banner">
        <div class="hero-content">
          <div class="mascot-avatar" title="น้องน็อต หุ่นยนต์นักประดิษฐ์">🤖</div>
          <div class="hero-text">
            <h2>สวัสดีนักประดิษฐ์ ม.1! มาไขความลับเครื่องกลกัน</h2>
            <p>
              "ลองเล่น ปรับค่า แล้วสังเกตผล" เครื่องกลแต่ละชนิดช่วยทุ่นแรงให้เราได้อย่างไร? 
              จำกฎเหล็กไว้เสมอ: <strong>"ได้แรงเพิ่ม แลกกับระยะทางที่ต้องใช้เพิ่ม" (งานเท่าเดิมเสมอ!)</strong>
            </p>
            <div class="hero-rule-pill">
              💡 กฎการอนุรักษ์พลังงาน: งานที่ได้ = แรงที่ออก × ระยะทางที่เคลื่อนที่ (W = F × s)
            </div>
          </div>
        </div>
      </div>

      <div class="machines-grid">

        <!-- CARD 1: คาน -->
        <div class="machine-card active-card">
          <div class="card-top">
            <div class="card-icon-box" style="background: #eff6ff; color: #2563eb;">⚖️</div>
            <div class="card-stars-earned">⭐ <span id="card-stars-lever">0</span> / 4</div>
          </div>
          <h3 class="card-title">1. คาน (Lever)</h3>
          <p class="card-subtitle">ปรับจุดหมุน วางตุ้มน้ำหนัก และเข้าใจโมเมนต์ของแรง คานอันดับ 1, 2 และ 3</p>
          <div class="card-formula-tag">M = แรง × ระยะจุดหมุน (M = F × L)</div>
          <button class="btn-enter-room" onclick="App.enterRoom('lever')">🚀 เข้าทดลองเล่นคาน</button>
        </div>

        <!-- CARD 2: รอก (เปิดใช้งานแล้ว!) -->
        <div class="machine-card active-card">
          <div class="card-top">
            <div class="card-icon-box" style="background: #fef3c7; color: #d97706;">🪢</div>
            <div class="card-stars-earned">⭐ <span id="card-stars-pulley">0</span> / 4</div>
          </div>
          <h3 class="card-title">2. รอก (Pulley)</h3>
          <p class="card-subtitle">รอกเดี่ยวตายตัว รอกเดี่ยวเคลื่อนที่ และรอกพวง ยิ่งมีเชือกช่วยแขวนมาก ยิ่งเบาแรง!</p>
          <div class="card-formula-tag">F = น้ำหนัก ÷ จำนวนเส้นเชือก (W ÷ n)</div>
          <button class="btn-enter-room" onclick="App.enterRoom('pulley')">🚀 เข้าทดลองเล่นรอก</button>
        </div>

        <!-- CARD 3: ทางลาด (เปิดใช้งานแล้ว!) -->
        <div class="machine-card active-card">
          <div class="card-top">
            <div class="card-icon-box" style="background: #f3e8ff; color: #7c3aed;">📐</div>
            <div class="card-stars-earned">⭐ <span id="card-stars-incline">0</span> / 4</div>
          </div>
          <h3 class="card-title">3. ทางลาด (Inclined Plane)</h3>
          <p class="card-subtitle">เข็นของขึ้นที่สูง ทางยาวและชันน้อยทุ่นแรงได้มหาศาล แลกกับต้องเข็นไกลขึ้น</p>
          <div class="card-formula-tag">F = W × (สูง ÷ ทางลาดยาว)</div>
          <button class="btn-enter-room" onclick="App.enterRoom('incline')">🚀 เข้าทดลองเล่นทางลาด</button>
        </div>

        <!-- CARD 4: เฟือง -->
        <div class="machine-card locked">
          <div class="card-top">
            <div class="card-icon-box" style="background: #ecfdf5; color: #059669;">⚙️</div>
            <div class="card-stars-earned">⭐ 0 / 4</div>
          </div>
          <h3 class="card-title">4. เฟือง (Gears)</h3>
          <p class="card-subtitle">ฟันเฟืองส่งต่อแรงหมุน อัตราทดของจำนวนฟัน อยากได้ความเร็วหรืออยากได้แรง?</p>
          <div class="card-formula-tag">อัตราทด = ฟันตาม ÷ ฟันขับ</div>
          <div class="badge-locked">⏳ กำลังเตรียมการในขั้นที่ 3</div>
        </div>

        <!-- CARD 5: แขนกล -->
        <div class="machine-card locked">
          <div class="card-top">
            <div class="card-icon-box" style="background: #fdf2f8; color: #db2777;">🦾</div>
            <div class="card-stars-earned">⭐ 0 / 4</div>
          </div>
          <h3 class="card-title">5. แขนกล (Robotic Arm)</h3>
          <p class="card-subtitle">รวมร่างคานหลายข้อต่อ บังคับมือจับคีบกล่องขึ้นชั้นวาง คานอันดับ 3 ที่ว่องไว</p>
          <div class="card-formula-tag">ระบบข้อต่อคานหลายท่อน</div>
          <div class="badge-locked">⏳ กำลังเตรียมการในขั้นที่ 3</div>
        </div>

      </div>

      <div class="summary-card">
        <div class="summary-info">
          <h3>🏆 ความก้าวหน้ารวมของฉัน: <span id="home-total-stars-text">0</span> ดาว</h3>
          <p>ผ่านภารกิจและทำควิซเพื่อสะสมดาวให้ครบ เป็นสุดยอดนักประดิษฐ์ ม.1</p>
        </div>
        <button class="btn-quick" onclick="App.resetProgress()" title="เริ่มบันทึกคะแนนใหม่ตั้งแต่ต้น">
          🔄 ล้างข้อมูลแล้วเริ่มเล่นใหม่
        </button>
      </div>

    </section>
''')

def write_lever_view(f):
    f.write('''
    <!-- ========================================================================
         VIEW 2: ROOM 1 - คาน (LEVER ROOM)
         ======================================================================== -->
    <section id="view-lever" class="view-section">
      <div class="room-header">
        <div class="room-title-area">
          <div class="room-icon">⚖️</div>
          <div>
            <h2>ห้องทดลอง: คาน (The Lever)</h2>
            <p>หลักการโมเมนต์ของแรง: หมุนทวนเข็ม = หมุนตามเข็ม (M_ทวน = M_ตาม)</p>
          </div>
        </div>
        <div class="room-tabs">
          <button class="tab-btn active" onclick="LeverLab.switchTab('explore')">🎮 <span>สำรวจอิสระ</span></button>
          <button class="tab-btn" onclick="LeverLab.switchTab('classes')">📚 <span>คาน 3 อันดับ</span></button>
          <button class="tab-btn" onclick="LeverLab.switchTab('predict')">🔮 <span>ลองทายก่อน</span></button>
          <button class="tab-btn" onclick="LeverLab.switchTab('missions')">🎯 <span>ภารกิจ (3)</span></button>
          <button class="tab-btn" onclick="LeverLab.switchTab('quiz')">📝 <span>ควิซท้ายห้อง</span></button>
        </div>
      </div>

      <!-- Tab Explore -->
      <div id="lever-tab-explore" class="tab-content-panel active">
        <div class="sim-layout">
          <div class="sim-stage-card">
            <div class="stage-status-bar">
              <div id="lever-balance-badge" class="balance-status-badge balanced">
                <span>⚖️</span> <span id="lever-status-text">คานอยู่ในสภาวะสมดุลพอดี!</span>
              </div>
              <div class="hint-drag-tag">👆 แตะลากลูกตุ้มหรือจุดหมุนบนคานได้เลย</div>
            </div>
            <div class="svg-container" id="lever-svg-container">
              <svg class="sim-svg" id="lever-svg" viewBox="0 0 760 380">
                <defs>
                  <filter id="lever-shadow" x="-10%" y="-10%" width="130%" height="130%">
                    <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.15" />
                  </filter>
                  <linearGradient id="beam-grad" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#94a3b8" /><stop offset="100%" stop-color="#64748b" />
                  </linearGradient>
                  <linearGradient id="fulcrum-grad" x1="0" y1="0" x2="1" y2="1">
                    <stop offset="0%" stop-color="#f87171" /><stop offset="100%" stop-color="#dc2626" />
                  </linearGradient>
                </defs>
                <line x1="40" y1="320" x2="720" y2="320" stroke="#cbd5e1" stroke-width="4" stroke-linecap="round" />
                <g id="ground-ticks" opacity="0.6"></g>
                <g id="fulcrum-group" style="cursor: ew-resize;">
                  <polygon points="0,0 -30,70 30,70" fill="url(#fulcrum-grad)" filter="url(#lever-shadow)" />
                  <circle cx="0" cy="0" r="7" fill="#ffffff" stroke="#991b1b" stroke-width="3" />
                  <text x="0" y="52" fill="#ffffff" font-family="Prompt" font-weight="700" font-size="14" text-anchor="middle">F (จุดหมุน)</text>
                </g>
                <g id="beam-rotating-group">
                  <rect id="main-beam" x="-320" y="-12" width="640" height="24" rx="6" fill="url(#beam-grad)" filter="url(#lever-shadow)" stroke="#475569" stroke-width="1.5" />
                  <g id="beam-ticks"></g>
                  <g id="left-weight-group" style="cursor: grab;">
                    <line x1="0" y1="12" x2="0" y2="45" stroke="#475569" stroke-width="2.5" stroke-dasharray="3,2" />
                    <rect id="left-box" x="-35" y="45" width="70" height="70" rx="8" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2.5" filter="url(#lever-shadow)" />
                    <text id="left-mass-text" x="0" y="78" fill="#ffffff" font-family="Prompt" font-weight="700" font-size="16" text-anchor="middle">6 kg</text>
                    <text id="left-force-text" x="0" y="98" fill="#dbeafe" font-family="Prompt" font-weight="500" font-size="12" text-anchor="middle">(60 N)</text>
                    <circle cx="0" cy="12" r="6" fill="#f59e0b" stroke="#ffffff" stroke-width="2" />
                  </g>
                  <g id="right-weight-group" style="cursor: grab;">
                    <line x1="0" y1="12" x2="0" y2="45" stroke="#475569" stroke-width="2.5" stroke-dasharray="3,2" />
                    <rect id="right-box" x="-35" y="45" width="70" height="70" rx="8" fill="#10b981" stroke="#059669" stroke-width="2.5" filter="url(#lever-shadow)" />
                    <text id="right-mass-text" x="0" y="78" fill="#ffffff" font-family="Prompt" font-weight="700" font-size="16" text-anchor="middle">2 kg</text>
                    <text id="right-force-text" x="0" y="98" fill="#d1fae5" font-family="Prompt" font-weight="500" font-size="12" text-anchor="middle">(20 N)</text>
                    <circle cx="0" cy="12" r="6" fill="#f59e0b" stroke="#ffffff" stroke-width="2" />
                  </g>
                </g>
              </svg>
            </div>
            <div class="stage-quick-actions">
              <span style="font-size: 0.85rem; font-weight: 600; color: var(--text-muted);">ตัวอย่างจัดคาน:</span>
              <button class="btn-quick" onclick="LeverLab.applyPreset('seesaw')">🎡 ไม้กระดก</button>
              <button class="btn-quick" onclick="LeverLab.applyPreset('heavy-rock')">🪨 งัดหิน 10 kg</button>
              <button class="btn-quick" onclick="LeverLab.applyPreset('balanced-diff')">⚖️ มวลต่างแต่สมดุล</button>
              <button class="btn-simulate-action" onclick="LeverLab.simulateLiftAnimation()">▶️ ลองกดคานเพื่อยก</button>
            </div>
          </div>

          <div class="side-controls-panel">
            <div class="control-group-card" style="border-top: 4px solid #3b82f6;">
              <div class="control-group-title">
                <span style="color: #1d4ed8; font-weight: 700;">📦 วัตถุฝั่งซ้าย (W)</span>
                <span id="tag-m-left" class="slider-val-tag">M = 0 N·m</span>
              </div>
              <div class="slider-row">
                <div class="slider-label-row"><span>น้ำหนัก (มวล)</span><span id="val-mass-left" class="slider-val-tag">6 kg</span></div>
                <input type="range" id="slider-mass-left" min="1" max="20" step="1" value="6" oninput="LeverLab.onControlChange()">
                <div class="stepper-box">
                  <button class="btn-step" onclick="LeverLab.stepValue('mass-left', -1)">-</button>
                  <button class="btn-step" onclick="LeverLab.stepValue('mass-left', 1)">+</button>
                </div>
              </div>
              <div class="slider-row">
                <div class="slider-label-row"><span>ระยะห่างจากจุดหมุน</span><span id="val-dist-left" class="slider-val-tag">1.0 m</span></div>
                <input type="range" id="slider-dist-left" min="0.2" max="3.0" step="0.1" value="1.0" oninput="LeverLab.onControlChange()">
              </div>
            </div>

            <div class="control-group-card" style="border-top: 4px solid #10b981;">
              <div class="control-group-title">
                <span style="color: #047857; font-weight: 700;">🖐️ แรงกดฝั่งขวา (E)</span>
                <span id="tag-m-right" class="slider-val-tag">M = 0 N·m</span>
              </div>
              <div class="slider-row">
                <div class="slider-label-row"><span>แรงกด (เทียบเท่าน้ำหนัก)</span><span id="val-mass-right" class="slider-val-tag">2 kg</span></div>
                <input type="range" id="slider-mass-right" min="1" max="20" step="1" value="2" oninput="LeverLab.onControlChange()">
                <div class="stepper-box">
                  <button class="btn-step" onclick="LeverLab.stepValue('mass-right', -1)">-</button>
                  <button class="btn-step" onclick="LeverLab.stepValue('mass-right', 1)">+</button>
                </div>
              </div>
              <div class="slider-row">
                <div class="slider-label-row"><span>ระยะห่างจากจุดหมุน</span><span id="val-dist-right" class="slider-val-tag">3.0 m</span></div>
                <input type="range" id="slider-dist-right" min="0.2" max="3.0" step="0.1" value="3.0" oninput="LeverLab.onControlChange()">
              </div>
            </div>

            <div class="control-group-card" style="border-top: 4px solid #ef4444;">
              <div class="control-group-title">
                <span style="color: #b91c1c; font-weight: 700;">📍 ตำแหน่งจุดหมุน (F)</span>
                <span id="val-fulcrum-pos" class="slider-val-tag">กึ่งกลาง (0.0 m)</span>
              </div>
              <input type="range" id="slider-fulcrum" min="-1.5" max="1.5" step="0.1" value="0.0" oninput="LeverLab.onControlChange()">
            </div>
          </div>
        </div>

        <div class="metrics-grid">
          <div class="metric-card">
            <div class="metric-icon-box" style="background: #eff6ff; color: #2563eb;">🔄</div>
            <div class="metric-info">
              <h4>โมเมนต์ทวนเข็ม (ซ้าย)</h4>
              <div id="metric-left-torque" class="metric-value">60 N·m</div>
              <div class="metric-desc">คำนวณจาก: 60 N × 1.0 m</div>
            </div>
          </div>
          <div class="metric-card">
            <div class="metric-icon-box" style="background: #ecfdf5; color: #059669;">🔃</div>
            <div class="metric-info">
              <h4>โมเมนต์ตามเข็ม (ขวา)</h4>
              <div id="metric-right-torque" class="metric-value">60 N·m</div>
              <div class="metric-desc">คำนวณจาก: 20 N × 3.0 m</div>
            </div>
          </div>
          <div class="metric-card">
            <div class="metric-icon-box" style="background: #fffbeb; color: #d97706;">⚡</div>
            <div class="metric-info">
              <h4>การได้เปรียบเชิงกล (M.A.)</h4>
              <div id="metric-ma" class="metric-value">3.0 เท่า</div>
              <div id="metric-ma-desc" class="metric-desc">ทุ่นแรงได้ 3 เท่า!</div>
            </div>
          </div>
          <div class="metric-card">
            <div class="metric-icon-box" id="metric-diff-icon" style="background: #f0fdf4; color: #16a34a;">🎯</div>
            <div class="metric-info">
              <h4>ความต่างโมเมนต์ (ΔM)</h4>
              <div id="metric-torque-diff" class="metric-value">0.0 N·m</div>
              <div id="metric-balance-summary" class="metric-desc">คานสมดุลพอดี ไม่เอียง</div>
            </div>
          </div>
        </div>

        <div class="work-conservation-card">
          <div class="work-icon">💡</div>
          <div class="work-text">
            <h4>กฎเหล็ก: "ได้แรงเพิ่ม แลกกับระยะทางที่ต้องใช้เพิ่ม" (งานเท่าเดิม!)</h4>
            <p id="work-explanation-text">
              ถ้ายกกล่องซ้ายขึ้น 0.20 เมตร ต้องกดฝั่งขวาลง 0.60 เมตร งานที่ทำ = 12 จูล (J) เท่ากันทั้งสองฝั่ง!
            </p>
          </div>
        </div>
      </div>

      <!-- Tab Classes -->
      <div id="lever-tab-classes" class="tab-content-panel">
        <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-bottom: 1rem;">
          <button class="btn-quick" id="btn-class-1" onclick="LeverLab.showClass(1)" style="flex:1;">🥇 คานอันดับ 1 (จุดหมุนกลาง)</button>
          <button class="btn-quick" id="btn-class-2" onclick="LeverLab.showClass(2)" style="flex:1;">🥈 คานอันดับ 2 (น้ำหนักกลาง)</button>
          <button class="btn-quick" id="btn-class-3" onclick="LeverLab.showClass(3)" style="flex:1;">🥉 คานอันดับ 3 (แรงพยายามกลาง)</button>
        </div>
        <div class="control-group-card" id="class-detail-view" style="padding: 1.5rem; margin-bottom: 1.5rem;"></div>
      </div>

      <!-- Tab Predict -->
      <div id="lever-tab-predict" class="tab-content-panel">
        <div class="predict-box">
          <div class="predict-header"><div class="predict-icon">🔮</div><div><h3>ลองทายผลเรื่องคาน</h3><p>เลือกคำตอบที่คิดว่าถูกต้อง แล้วกดรันเพื่อดูของจริง</p></div></div>
          <div class="predict-scenario-card"><h4 id="predict-question-title" style="color: #1e3a8a; margin-bottom: 0.5rem;"></h4><p id="predict-question-desc"></p></div>
          <div class="predict-options-list" id="predict-options-container"></div>
          <div style="display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
            <button id="btn-run-prediction" class="btn-run-prediction" disabled onclick="LeverLab.executePredictionTest()">▶️ รันดูการทดลองจริง</button>
            <button class="btn-quick" onclick="LeverLab.nextPredictionScenario()">⏭️ สถานการณ์ถัดไป</button>
          </div>
          <div id="predict-result-box" class="predict-result-box"><h4 id="predict-feedback-title"></h4><p id="predict-feedback-text"></p></div>
        </div>
      </div>

      <!-- Tab Missions -->
      <div id="lever-tab-missions" class="tab-content-panel">
        <div class="missions-container">
          <div class="mission-card" id="mission-card-1">
            <div class="mission-header"><span class="mission-num-badge">ภารกิจที่ 1</span><span class="mission-star-award" id="mstar-1">⭐</span></div>
            <h4 class="mission-title">🌟 สมดุลคานด้วยลูกตุ้ม 2 กก.</h4>
            <p class="mission-desc">มีกล่อง 6 กก. ห่างจุดหมุน 1.0 ม. ทางซ้าย จงปรับตำแหน่งลูกตุ้ม 2 กก. ให้คานสมดุลพอดี!</p>
            <div class="mission-actions"><button class="btn-apply-mission" onclick="LeverLab.loadMission(1)">🛠️ จัดฉาก</button><button class="btn-check-mission" onclick="LeverLab.checkMission(1)">✅ ตรวจสอบ</button></div>
            <div class="mission-feedback" id="mission-fb-1"></div>
          </div>
          <div class="mission-card" id="mission-card-2">
            <div class="mission-header"><span class="mission-num-badge">ภารกิจที่ 2</span><span class="mission-star-award" id="mstar-2">⭐</span></div>
            <h4 class="mission-title">🌟🌟 งัดหิน 12 กก. ด้วยแรงไม่เกิน 3 กก.</h4>
            <p class="mission-desc">ต้องการงัดหินหนัก 12 กก. (ระยะ 0.5 ม.) โดยออกแรงกดไม่เกิน 3 กก. จงปรับระยะทางขวาให้งัดขึ้นได้!</p>
            <div class="mission-actions"><button class="btn-apply-mission" onclick="LeverLab.loadMission(2)">🛠️ จัดฉาก</button><button class="btn-check-mission" onclick="LeverLab.checkMission(2)">✅ ตรวจสอบ</button></div>
            <div class="mission-feedback" id="mission-fb-2"></div>
          </div>
          <div class="mission-card" id="mission-card-3">
            <div class="mission-header"><span class="mission-num-badge">ภารกิจที่ 3</span><span class="mission-star-award" id="mstar-3">⭐</span></div>
            <h4 class="mission-title">🌟🌟🌟 ปริศนารถเข็นทราย (คานอันดับ 2)</h4>
            <p class="mission-desc">กองดินหนัก 18 กก. อยู่ห่างล้อหน้า 0.8 ม. ถ้าด้ามจับอยู่ที่ 2.4 ม. ต้องออกแรงกี่กิโลกรัมจึงจะยกขึ้นพอดี?</p>
            <div class="mission-actions"><button class="btn-apply-mission" onclick="LeverLab.loadMission(3)">🛠️ จัดฉาก</button><button class="btn-check-mission" onclick="LeverLab.checkMission(3)">✅ ตรวจสอบ</button></div>
            <div class="mission-feedback" id="mission-fb-3"></div>
          </div>
        </div>
      </div>

      <!-- Tab Quiz -->
      <div id="lever-tab-quiz" class="tab-content-panel">
        <div class="quiz-container">
          <h3 style="margin-bottom: 1rem;">📝 แบบทดสอบความเข้าใจเรื่องคาน (4 ข้อ)</h3>
          <form id="lever-quiz-form" onsubmit="event.preventDefault(); LeverLab.submitQuiz();">
            <div class="quiz-question-item">
              <div class="quiz-q-title"><strong>ข้อ 1.</strong><span>หลักการสำคัญที่สุดของเครื่องกลอย่างง่ายที่ถูกต้องคือข้อใด?</span></div>
              <div class="quiz-choices">
                <label class="quiz-choice-label"><input type="radio" name="lq1" value="a" required><span>ก. ช่วยลดงานทั้งหมดที่เราต้องทำให้เป็นศูนย์</span></label>
                <label class="quiz-choice-label"><input type="radio" name="lq1" value="b"><span>ข. ช่วยผ่อนแรงที่ต้องออก แลกกับระยะทางที่เคลื่อนที่มากขึ้น (งานเท่าเดิม)</span></label>
                <label class="quiz-choice-label"><input type="radio" name="lq1" value="c"><span>ค. ช่วยสร้างพลังงานใหม่ให้แก่วัตถุ</span></label>
              </div>
              <div class="quiz-explanation" id="exp-lq1">💡 <strong>เฉลย ข:</strong> ถูกต้อง! งานยังคงเท่าเดิมเสมอ หากออกแรงน้อยลงต้องแลกกับระยะทางที่มากขึ้น</div>
            </div>
            <div class="quiz-question-item">
              <div class="quiz-q-title"><strong>ข้อ 2.</strong><span>เครื่องมือใดจัดเป็น <strong>"คานอันดับ 1"</strong> (จุดหมุนอยู่ระหว่างแรงและน้ำหนัก)?</span></div>
              <div class="quiz-choices">
                <label class="quiz-choice-label"><input type="radio" name="lq2" value="a" required><span>ก. กรรไกร และ ไม้กระดก</span></label>
                <label class="quiz-choice-label"><input type="radio" name="lq2" value="b"><span>ข. รถเข็นทราย และ ที่เปิดขวด</span></label>
                <label class="quiz-choice-label"><input type="radio" name="lq2" value="c"><span>ค. ตะเกียบ และ คีมคีบน้ำแข็ง</span></label>
              </div>
              <div class="quiz-explanation" id="exp-lq2">💡 <strong>เฉลย ก:</strong> ถูกต้อง! กรรไกรและไม้กระดกมีจุดหมุน (F) อยู่ตรงกลาง</div>
            </div>
            <div class="quiz-question-item">
              <div class="quiz-q-title"><strong>ข้อ 3.</strong><span>ถ้าต้องการใช้งัดหินหนักให้ <strong>"ทุ่นแรงได้มากที่สุด"</strong> ควรจัดตำแหน่งอย่างไร?</span></div>
              <div class="quiz-choices">
                <label class="quiz-choice-label"><input type="radio" name="lq3" value="a" required><span>ก. จุดหมุนชิดก้อนหินที่สุด และกดมือที่ปลายไกลที่สุด</span></label>
                <label class="quiz-choice-label"><input type="radio" name="lq3" value="b"><span>ข. จุดหมุนอยู่ตรงกลางคานพอดี</span></label>
                <label class="quiz-choice-label"><input type="radio" name="lq3" value="c"><span>ค. จุดหมุนใกล้จุดที่มือกดมากที่สุด</span></label>
              </div>
              <div class="quiz-explanation" id="exp-lq3">💡 <strong>เฉลย ก:</strong> ถูกต้อง! เพื่อให้แขนแรงยาวที่สุด และแขนน้ำหนักสั้นที่สุด</div>
            </div>
            <div class="quiz-question-item">
              <div class="quiz-q-title"><strong>ข้อ 4.</strong><span>ทำไม <strong>คานอันดับ 2</strong> (เช่น รถเข็นทราย) จึงทุ่นแรงเสมอ (M.A. > 1)?</span></div>
              <div class="quiz-choices">
                <label class="quiz-choice-label"><input type="radio" name="lq4" value="a" required><span>ก. เพราะน้ำหนัก (W) อยู่ตรงกลาง ทำให้แขนแรงยาวกว่าแขนน้ำหนักเสมอ</span></label>
                <label class="quiz-choice-label"><input type="radio" name="lq4" value="b"><span>ข. เพราะทำจากโลหะที่แข็งแรง</span></label>
                <label class="quiz-choice-label"><input type="radio" name="lq4" value="c"><span>ค. เพราะจุดหมุนอยู่ตรงกลางเสมอ</span></label>
              </div>
              <div class="quiz-explanation" id="exp-lq4">💡 <strong>เฉลย ก:</strong> ถูกต้อง! แขนแรงพยายามอยู่ปลายสุดจึงยาวกว่าแขนน้ำหนักเสมอ</div>
            </div>
            <div class="quiz-footer">
              <button type="submit" class="btn-check-mission">📝 ส่งคำตอบและตรวจคะแนน</button>
              <div id="lever-quiz-summary" class="quiz-score-badge"></div>
            </div>
          </form>
        </div>
      </div>
    </section>
''')

def write_pulley_view(f):
    f.write('''
    <!-- ========================================================================
         VIEW 3: ROOM 2 - รอก (PULLEY ROOM)
         ======================================================================== -->
    <section id="view-pulley" class="view-section">
      <div class="room-header">
        <div class="room-title-area">
          <div class="room-icon">🪢</div>
          <div>
            <h2>ห้องทดลอง: รอก (The Pulley)</h2>
            <p>สูตรผ่อนแรง: แรงดึง = น้ำหนัก ÷ จำนวนเส้นเชือกรับน้ำหนัก (F = W ÷ n)</p>
          </div>
        </div>
        <div class="room-tabs">
          <button class="tab-btn active" onclick="PulleyLab.switchTab('explore')">🎮 <span>สำรวจอิสระ</span></button>
          <button class="tab-btn" onclick="PulleyLab.switchTab('types')">📚 <span>ชนิดของรอก</span></button>
          <button class="tab-btn" onclick="PulleyLab.switchTab('predict')">🔮 <span>ลองทายก่อน</span></button>
          <button class="tab-btn" onclick="PulleyLab.switchTab('missions')">🎯 <span>ภารกิจ (3)</span></button>
          <button class="tab-btn" onclick="PulleyLab.switchTab('quiz')">📝 <span>ควิซท้ายห้อง</span></button>
        </div>
      </div>

      <!-- Tab Explore -->
      <div id="pulley-tab-explore" class="tab-content-panel active">
        <div class="sim-layout">
          <div class="sim-stage-card">
            <div class="stage-status-bar">
              <div id="pulley-status-badge" class="balance-status-badge balanced">
                <span>🪢</span> <span id="pulley-status-text">พร้อมดึงเชือกยกของ!</span>
              </div>
              <div class="hint-drag-tag">👆 แตะลากมือจับเชือกดึงลงได้เลย</div>
            </div>

            <!-- SVG STAGE FOR PULLEY -->
            <div class="svg-container" id="pulley-svg-container">
              <svg class="sim-svg" id="pulley-svg" viewBox="0 0 760 380">
                <defs>
                  <filter id="pulley-shadow" x="-10%" y="-10%" width="130%" height="130%">
                    <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.18" />
                  </filter>
                  <linearGradient id="pulley-metal" x1="0" y1="0" x2="1" y2="1">
                    <stop offset="0%" stop-color="#cbd5e1" /><stop offset="100%" stop-color="#64748b" />
                  </linearGradient>
                  <linearGradient id="pulley-hub" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#f87171" /><stop offset="100%" stop-color="#b91c1c" />
                  </linearGradient>
                </defs>

                <!-- Ceiling Beam Structure -->
                <rect x="60" y="16" width="640" height="18" rx="4" fill="#334155" filter="url(#pulley-shadow)" />
                <line x1="60" y1="34" x2="700" y2="34" stroke="#475569" stroke-width="2" />
                <!-- Hatch pattern for ceiling -->
                <g stroke="#64748b" stroke-width="2" opacity="0.6">
                  <line x1="80" y1="16" x2="95" y2="6" /><line x1="140" y1="16" x2="155" y2="6" />
                  <line x1="200" y1="16" x2="215" y2="6" /><line x1="260" y1="16" x2="275" y2="6" />
                  <line x1="320" y1="16" x2="335" y2="6" /><line x1="380" y1="16" x2="395" y2="6" />
                  <line x1="440" y1="16" x2="455" y2="6" /><line x1="500" y1="16" x2="515" y2="6" />
                  <line x1="560" y1="16" x2="575" y2="6" /><line x1="620" y1="16" x2="635" y2="6" />
                  <line x1="680" y1="16" x2="695" y2="6" />
                </g>

                <!-- Ground Floor -->
                <line x1="60" y1="340" x2="700" y2="340" stroke="#cbd5e1" stroke-width="4" stroke-linecap="round" />

                <!-- DYNAMIC PULLEY GRAPHICS (Rendered by PulleyLab.render()) -->
                <g id="pulley-dynamic-layer"></g>

                <!-- Height and Distance Scale annotations -->
                <g id="pulley-scale-layer"></g>
              </svg>
            </div>

            <div class="stage-quick-actions">
              <span style="font-size: 0.85rem; font-weight: 600; color: var(--text-muted);">การทดลองด่วน:</span>
              <button class="btn-quick" onclick="PulleyLab.setPreset('fixed')">🏛️ รอกเดี่ยวตายตัว (ธงชาติ)</button>
              <button class="btn-quick" onclick="PulleyLab.setPreset('movable')">🏗️ รอกเดี่ยวเคลื่อนที่ (ทุ่นแรงครึ่ง)</button>
              <button class="btn-quick" onclick="PulleyLab.setPreset('compound-4')">🚢 รอกพวง 4 เส้น (เครนยักษ์)</button>
              <button class="btn-simulate-action" onclick="PulleyLab.simulatePullAnimation()">▶️ ดึงเชือกยกของ</button>
            </div>
          </div>

          <!-- Controls Side Panel -->
          <div class="side-controls-panel">
            
            <!-- Pulley Type Selector -->
            <div class="control-group-card" style="border-top: 4px solid var(--accent);">
              <div class="control-group-title">
                <span style="color: var(--accent-dark); font-weight: 700;">⚙️ เลือกชนิดของรอก</span>
              </div>
              <div class="pill-selector" style="margin-bottom: 0.75rem;">
                <button class="pill-btn active" id="btn-ptype-fixed" onclick="PulleyLab.setType('fixed')">ตายตัว</button>
                <button class="pill-btn" id="btn-ptype-movable" onclick="PulleyLab.setType('movable')">เคลื่อนที่</button>
                <button class="pill-btn" id="btn-ptype-compound" onclick="PulleyLab.setType('compound')">รอกพวง</button>
              </div>

              <!-- Compound strand count (Only when type is compound) -->
              <div id="compound-strand-row" style="display: none; margin-top: 0.5rem; background: #fffbeb; padding: 0.6rem; border-radius: var(--radius-sm); border: 1px solid #fde68a;">
                <div class="slider-label-row">
                  <span style="font-size: 0.85rem; color: #92400e;">จำนวนเส้นเชือกรับน้ำหนัก (n):</span>
                  <span id="val-pulley-strands" class="slider-val-tag" style="color: #b45309;">4 เส้น</span>
                </div>
                <input type="range" id="slider-pulley-strands" min="2" max="6" step="1" value="4" oninput="PulleyLab.onStrandChange()">
                <div style="display: flex; justify-content: space-between; font-size: 0.75rem; color: #92400e; margin-top: 0.2rem;">
                  <span>2 เส้น (เบา 2 เท่า)</span>
                  <span>4 เส้น</span>
                  <span>6 เส้น (เบา 6 เท่า)</span>
                </div>
              </div>
            </div>

            <!-- Load Weight Slider -->
            <div class="control-group-card" style="border-top: 4px solid #3b82f6;">
              <div class="control-group-title">
                <span style="color: #1d4ed8; font-weight: 700;">📦 น้ำหนักวัตถุที่ต้องการยก (W)</span>
                <span id="tag-pulley-weight" class="slider-val-tag">60 kg (600 N)</span>
              </div>
              <div class="slider-row">
                <input type="range" id="slider-pulley-mass" min="10" max="100" step="5" value="60" oninput="PulleyLab.onControlChange()">
                <div class="stepper-box">
                  <button class="btn-step" onclick="PulleyLab.stepMass(-10)">-10</button>
                  <button class="btn-step" onclick="PulleyLab.stepMass(10)">+10</button>
                  <span style="font-size: 0.8rem; color: var(--text-muted); margin-left: auto;">ปรับได้ 10 - 100 กก.</span>
                </div>
              </div>
            </div>

            <!-- Pull / Lift Slider -->
            <div class="control-group-card" style="border-top: 4px solid #10b981;">
              <div class="control-group-title">
                <span style="color: #047857; font-weight: 700;">📏 ระยะความสูงที่ยกของขึ้น (h)</span>
                <span id="tag-pulley-height" class="slider-val-tag">0.60 ม.</span>
              </div>
              <div class="slider-row">
                <input type="range" id="slider-pulley-height" min="0.0" max="1.6" step="0.05" value="0.6" oninput="PulleyLab.onControlChange()">
                <div style="display: flex; justify-content: space-between; font-size: 0.75rem; color: var(--text-muted); margin-top: 0.2rem;">
                  <span>0 ม. (วางบนพื้น)</span>
                  <span>ยกขึ้นสูงสุด 1.6 ม.</span>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- Metrics Dashboard -->
        <div class="metrics-grid">
          <div class="metric-card">
            <div class="metric-icon-box" style="background: #eff6ff; color: #2563eb;">📦</div>
            <div class="metric-info">
              <h4>น้ำหนักของ (W)</h4>
              <div id="metric-pulley-w" class="metric-value">60 kg</div>
              <div id="metric-pulley-w-desc" class="metric-desc">แรงโน้มถ่วง = 600 N</div>
            </div>
          </div>
          <div class="metric-card">
            <div class="metric-icon-box" style="background: #ecfdf5; color: #059669;">🖐️</div>
            <div class="metric-info">
              <h4>แรงดึงที่ต้องออก (F)</h4>
              <div id="metric-pulley-f" class="metric-value">15 kg (150 N)</div>
              <div id="metric-pulley-f-desc" class="metric-desc">ทุ่นแรงได้มหาศาล!</div>
            </div>
          </div>
          <div class="metric-card">
            <div class="metric-icon-box" style="background: #fffbeb; color: #d97706;">⚡</div>
            <div class="metric-info">
              <h4>การได้เปรียบเชิงกล (M.A.)</h4>
              <div id="metric-pulley-ma" class="metric-value">4.0 เท่า</div>
              <div id="metric-pulley-ma-desc" class="metric-desc">มีเชือก 4 เส้นช่วยพยุง</div>
            </div>
          </div>
          <div class="metric-card">
            <div class="metric-icon-box" style="background: #fdf2f8; color: #db2777;">📏</div>
            <div class="metric-info">
              <h4>ระยะเชือกที่ต้องดึง (s)</h4>
              <div id="metric-pulley-s" class="metric-value">2.40 ม.</div>
              <div id="metric-pulley-s-desc" class="metric-desc">ยกของสูง 0.60 ม. × 4</div>
            </div>
          </div>
        </div>

        <!-- Work Conservation Banner -->
        <div class="work-conservation-card">
          <div class="work-icon">💡</div>
          <div class="work-text">
            <h4>กฎของงาน: "ออกแรงดึงเบาลง แลกกับต้องสาวเชือกยาวขึ้น" (งานเท่าเดิม!)</h4>
            <p id="work-pulley-explanation">
              ในการยกกล่อง 600 N สูง 0.60 ม. งานที่ได้ = <strong>360 จูล (J)</strong><br>
              เมื่อใช้รอกพวง 4 เส้น เราออกแรงดึงเพียง 150 N แต่ต้องดึงเชือกยาว 2.40 ม. 
              งานที่เราทำ = 150 N × 2.40 ม. = <strong>360 จูล (J) เท่ากันเป๊ะ!</strong>
            </p>
          </div>
        </div>
      </div>

      <!-- Tab Types (ความรู้เรื่องรอก) -->
      <div id="pulley-tab-types" class="tab-content-panel">
        <div class="knowledge-box">
          <h3 class="knowledge-title">📖 เจาะลึกรอก 3 ชนิดในวิชาวิทยาศาสตร์ ม.1</h3>
          <div class="knowledge-grid">
            <div class="knowledge-item" style="border-left-color: #3b82f6;">
              <h5>1. รอกเดี่ยวตายตัว (Fixed Pulley)</h5>
              <p>
                <strong>จุดเด่น:</strong> ตัวรอกถูกตรึงอยู่กับที่ (เช่น ยอดเสาธง, รอกยกถังปูน)<br>
                <strong>การทุ่นแรง:</strong> <strong>ไม่ช่วยผ่อนแรง (M.A. = 1)</strong> ออกแรงเท่ากับน้ำหนักของ<br>
                <strong>ประโยชน์:</strong> ช่วย<strong>เปลี่ยนทิศทางของแรง</strong> ให้เราออกแรงดึงลงตามแรงโน้มถ่วง ซึ่งสะดวกและปลอดภัยกว่ายกขึ้นตรงๆ
              </p>
            </div>
            <div class="knowledge-item" style="border-left-color: #10b981;">
              <h5>2. รอกเดี่ยวเคลื่อนที่ (Movable Pulley)</h5>
              <p>
                <strong>จุดเด่น:</strong> ตัวรอกแขวนอยู่กับเชือกและเคลื่อนที่ขึ้นลงพร้อมกับวัตถุ<br>
                <strong>การทุ่นแรง:</strong> <strong>ช่วยผ่อนแรงครึ่งหนึ่งเสมอ (M.A. = 2)</strong> แรงดึง F = W ÷ 2<br>
                <strong>ระยะทาง:</strong> ต้องดึงเชือกเป็นระยะทาง <strong>2 เท่า</strong> ของความสูงที่วัตถุลอยขึ้น (s = 2h)
              </p>
            </div>
            <div class="knowledge-item" style="border-left-color: #f59e0b;">
              <h5>3. รอกพวง (Compound Pulley / Block & Tackle)</h5>
              <p>
                <strong>จุดเด่น:</strong> รวมรอกเดี่ยวตายตัวและรอกเดี่ยวเคลื่อนที่เข้าด้วยกันเป็นตลับ (เช่น ปั้นจั่น, เครนยกของ)<br>
                <strong>การทุ่นแรง:</strong> <strong>F = W ÷ n</strong> (เมื่อ n คือจำนวนเส้นเชือกที่รับน้ำหนักวัตถุ)<br>
                <strong>หัวใจสำคัญ:</strong> ยิ่งมีเชือกช่วยหิ้วมาก ยิ่งเบาแรง แต่ต้องสาวเชือกยาวขึ้นเป็น n เท่าตัว!
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Tab Predict -->
      <div id="pulley-tab-predict" class="tab-content-panel">
        <div class="predict-box">
          <div class="predict-header"><div class="predict-icon">🔮</div><div><h3>ลองทายผลเรื่องรอก</h3><p>เลือกคำตอบที่คิดว่าถูกต้อง แล้วกดรันเพื่อดูของจริง</p></div></div>
          <div class="predict-scenario-card"><h4 id="pulley-predict-q-title" style="color: #1e3a8a; margin-bottom: 0.5rem;"></h4><p id="pulley-predict-q-desc"></p></div>
          <div class="predict-options-list" id="pulley-predict-options-container"></div>
          <div style="display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
            <button id="btn-run-pulley-predict" class="btn-run-prediction" disabled onclick="PulleyLab.executePredictionTest()">▶️ รันดูการทดลองจริง</button>
            <button class="btn-quick" onclick="PulleyLab.nextPredictionScenario()">⏭️ สถานการณ์ถัดไป</button>
          </div>
          <div id="pulley-predict-result-box" class="predict-result-box"><h4 id="pulley-predict-fb-title"></h4><p id="pulley-predict-fb-text"></p></div>
        </div>
      </div>

      <!-- Tab Missions -->
      <div id="pulley-tab-missions" class="tab-content-panel">
        <div class="missions-container">
          <div class="mission-card" id="pmission-card-1">
            <div class="mission-header"><span class="mission-num-badge">ภารกิจที่ 1</span><span class="mission-star-award" id="pmstar-1">⭐</span></div>
            <h4 class="mission-title">🌟 มือใหม่รอกเดี่ยวเคลื่อนที่</h4>
            <p class="mission-desc">มีกล่องหนัก <strong>30 กก.</strong> จงตั้งค่ารอกให้ใช้แรงดึงเพียง <strong>15 กก.</strong> (ผ่อนแรงครึ่งหนึ่ง)!</p>
            <div class="mission-actions"><button class="btn-apply-mission" onclick="PulleyLab.loadMission(1)">🛠️ จัดฉาก</button><button class="btn-check-mission" onclick="PulleyLab.checkMission(1)">✅ ตรวจสอบ</button></div>
            <div class="mission-feedback" id="pmission-fb-1"></div>
          </div>
          <div class="mission-card" id="pmission-card-2">
            <div class="mission-header"><span class="mission-num-badge">ภารกิจที่ 2</span><span class="mission-star-award" id="pmstar-2">⭐</span></div>
            <h4 class="mission-title">🌟🌟 ยกกล่องหนัก 60 กก. ด้วยแรงไม่เกิน 15 กก.</h4>
            <p class="mission-desc">ต้องการยกกล่องหนัก <strong>60 กก.</strong> โดยคุณมีแรงดึงจำกัด <strong>ไม่เกิน 15 กก.</strong> จงเลือกรอกพวงและจำนวนเส้นเชือกให้เหมาะสม!</p>
            <div class="mission-actions"><button class="btn-apply-mission" onclick="PulleyLab.loadMission(2)">🛠️ จัดฉาก</button><button class="btn-check-mission" onclick="PulleyLab.checkMission(2)">✅ ตรวจสอบ</button></div>
            <div class="mission-feedback" id="pmission-fb-2"></div>
          </div>
          <div class="mission-card" id="pmission-card-3">
            <div class="mission-header"><span class="mission-num-badge">ภารกิจที่ 3</span><span class="mission-star-award" id="pmstar-3">⭐</span></div>
            <h4 class="mission-title">🌟🌟🌟 พิสูจน์กฎของงาน (50 กก. สูง 1.2 ม.)</h4>
            <p class="mission-desc">ใช้รอกพวง 5 เส้น ยกของหนัก <strong>50 กก.</strong> ให้ลอยสูงขึ้น <strong>1.2 เมตร</strong> จงคำนวณและตรวจสอบระยะเชือกและงานที่ทำ!</p>
            <div class="mission-actions"><button class="btn-apply-mission" onclick="PulleyLab.loadMission(3)">🛠️ จัดฉาก</button><button class="btn-check-mission" onclick="PulleyLab.checkMission(3)">✅ ตรวจสอบ</button></div>
            <div class="mission-feedback" id="pmission-fb-3"></div>
          </div>
        </div>
      </div>

      <!-- Tab Quiz -->
      <div id="pulley-tab-quiz" class="tab-content-panel">
        <div class="quiz-container">
          <h3 style="margin-bottom: 1rem;">📝 แบบทดสอบความเข้าใจเรื่องรอก (4 ข้อ)</h3>
          <form id="pulley-quiz-form" onsubmit="event.preventDefault(); PulleyLab.submitQuiz();">
            <div class="quiz-question-item">
              <div class="quiz-q-title"><strong>ข้อ 1.</strong><span>รอกเดี่ยวตายตัว (เช่น รอกเชิญธงชาติ) มีประโยชน์หลักทางวิทยาศาสตร์อย่างไร?</span></div>
              <div class="quiz-choices">
                <label class="quiz-choice-label"><input type="radio" name="pq1" value="a" required><span>ก. ช่วยลดแรงที่ต้องดึงลงครึ่งหนึ่ง</span></label>
                <label class="quiz-choice-label"><input type="radio" name="pq1" value="b"><span>ข. ช่วยเปลี่ยนทิศทางของแรงให้ออกแรงดึงได้สะดวกขึ้น แม้ไม่ทุ่นแรง</span></label>
                <label class="quiz-choice-label"><input type="radio" name="pq1" value="c"><span>ค. ช่วยลดงานทั้งหมดที่เราต้องทำให้น้อยลง</span></label>
              </div>
              <div class="quiz-explanation" id="exp-pq1">💡 <strong>เฉลย ข:</strong> ถูกต้อง! รอกเดี่ยวตายตัว M.A. = 1 ไม่ผ่อนแรง แต่อำนวยความสะดวกในการเปลี่ยนทิศทางแรง</div>
            </div>
            <div class="quiz-question-item">
              <div class="quiz-q-title"><strong>ข้อ 2.</strong><span>รอกเดี่ยวเคลื่อนที่สามารถช่วยผ่อนแรงได้อย่างไร?</span></div>
              <div class="quiz-choices">
                <label class="quiz-choice-label"><input type="radio" name="pq2" value="a" required><span>ก. ผ่อนแรงครึ่งหนึ่ง (F = W ÷ 2) เพราะมีเชือก 2 เส้นช่วยพยุงน้ำหนัก</span></label>
                <label class="quiz-choice-label"><input type="radio" name="pq2" value="b"><span>ข. ไม่ผ่อนแรงเลยเหมือนรอกตายตัว</span></label>
                <label class="quiz-choice-label"><input type="radio" name="pq2" value="c"><span>ค. ผ่อนแรงได้ถึง 4 เท่าเสมอ</span></label>
              </div>
              <div class="quiz-explanation" id="exp-pq2">💡 <strong>เฉลย ก:</strong> ถูกต้อง! เชือก 2 เส้นแบ่งรับน้ำหนักคนละครึ่ง จึงออกแรงเพียง W/2</div>
            </div>
            <div class="quiz-question-item">
              <div class="quiz-q-title"><strong>ข้อ 3.</strong><span>ถ้าต้องการยกตู้เซฟหนัก 1,000 N ด้วยแรงเพียง 250 N ต้องใช้รอกพวงที่มีเชือกรับน้ำหนักกี่เส้น?</span></div>
              <div class="quiz-choices">
                <label class="quiz-choice-label"><input type="radio" name="pq3" value="a" required><span>ก. 2 เส้น</span></label>
                <label class="quiz-choice-label"><input type="radio" name="pq3" value="b"><span>ข. 4 เส้น (เพราะ 1,000 ÷ 4 = 250 N)</span></label>
                <label class="quiz-choice-label"><input type="radio" name="pq3" value="c"><span>ค. 8 เส้น</span></label>
              </div>
              <div class="quiz-explanation" id="exp-pq3">💡 <strong>เฉลย ข:</strong> ถูกต้อง! จำนวนเส้นเชือก n = W ÷ F = 1000 ÷ 250 = 4 เส้น</div>
            </div>
            <div class="quiz-question-item">
              <div class="quiz-q-title"><strong>ข้อ 4.</strong><span>ในการใช้รอกพวง 5 เส้น ยกของหนักขึ้นสูง 2 เมตร เราจะต้องดึงเชือกเป็นระยะทางเท่าใด?</span></div>
              <div class="quiz-choices">
                <label class="quiz-choice-label"><input type="radio" name="pq4" value="a" required><span>ก. 2 เมตร เท่าเดิม</span></label>
                <label class="quiz-choice-label"><input type="radio" name="pq4" value="b"><span>ข. 5 เมตร</span></label>
                <label class="quiz-choice-label"><input type="radio" name="pq4" value="c"><span>ค. 10 เมตร (ระยะเชือก s = n × h = 5 × 2 ม.)</span></label>
              </div>
              <div class="quiz-explanation" id="exp-pq4">💡 <strong>เฉลย ค:</strong> ถูกต้อง! ได้แรงเพิ่ม 5 เท่า แลกกับต้องดึงเชือกยาวขึ้น 5 เท่า (s = 5 × 2 = 10 ม.) ตามกฎของงาน!</div>
            </div>
            <div class="quiz-footer">
              <button type="submit" class="btn-check-mission">📝 ส่งคำตอบและตรวจคะแนน</button>
              <div id="pulley-quiz-summary" class="quiz-score-badge"></div>
            </div>
          </form>
        </div>
      </div>
    </section>
''')

def write_incline_view(f):
    f.write('''
    <!-- ========================================================================
         VIEW 4: ROOM 3 - ทางลาด (INCLINED PLANE ROOM)
         ======================================================================== -->
    <section id="view-incline" class="view-section">
      <div class="room-header">
        <div class="room-title-area">
          <div class="room-icon">📐</div>
          <div>
            <h2>ห้องทดลอง: ทางลาด (The Inclined Plane)</h2>
            <p>สูตรผ่อนแรง: แรงดัน F = น้ำหนัก × (ความสูง ÷ ความยาวทางลาด) (F = W × h ÷ L)</p>
          </div>
        </div>
        <div class="room-tabs">
          <button class="tab-btn active" onclick="InclineLab.switchTab('explore')">🎮 <span>สำรวจอิสระ</span></button>
          <button class="tab-btn" onclick="InclineLab.switchTab('realworld')">📚 <span>ทางลาดในชีวิตจริง</span></button>
          <button class="tab-btn" onclick="InclineLab.switchTab('predict')">🔮 <span>ลองทายก่อน</span></button>
          <button class="tab-btn" onclick="InclineLab.switchTab('missions')">🎯 <span>ภารกิจ (3)</span></button>
          <button class="tab-btn" onclick="InclineLab.switchTab('quiz')">📝 <span>ควิซท้ายห้อง</span></button>
        </div>
      </div>

      <!-- Tab Explore -->
      <div id="incline-tab-explore" class="tab-content-panel active">
        <div class="sim-layout">
          <div class="sim-stage-card">
            <div class="stage-status-bar">
              <div id="incline-status-badge" class="balance-status-badge balanced">
                <span>📐</span> <span id="incline-status-text">ทางลาดพร้อมทดลอง!</span>
              </div>
              <div class="hint-drag-tag">👆 แตะลากรถเข็นขึ้นลงบนทางลาดได้เลย</div>
            </div>

            <!-- SVG STAGE FOR INCLINE -->
            <div class="svg-container" id="incline-svg-container">
              <svg class="sim-svg" id="incline-svg" viewBox="0 0 760 380">
                <defs>
                  <filter id="incline-shadow" x="-10%" y="-10%" width="130%" height="130%">
                    <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.15" />
                  </filter>
                  <linearGradient id="ramp-grad" x1="0" y1="0" x2="1" y2="1">
                    <stop offset="0%" stop-color="#eff6ff" /><stop offset="100%" stop-color="#bfdbfe" />
                  </linearGradient>
                </defs>

                <!-- Ground Floor -->
                <line x1="40" y1="330" x2="720" y2="330" stroke="#cbd5e1" stroke-width="4" stroke-linecap="round" />

                <!-- Triangular Ramp Polygon (Dynamic) -->
                <polygon id="ramp-triangle" points="100,330 620,330 620,150" fill="url(#ramp-grad)" stroke="#2563eb" stroke-width="2.5" filter="url(#incline-shadow)" />

                <!-- Truck or Platform Icon on Top Right -->
                <g id="truck-platform-group">
                  <rect id="top-platform" x="620" y="150" width="100" height="180" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2" />
                  <text id="top-platform-label" x="670" y="240" fill="#64748b" font-family="Prompt" font-size="13" font-weight="600" text-anchor="middle">ท้ายรถบรรทุก</text>
                </g>

                <!-- Dimension Lines & Labels -->
                <g id="incline-dimensions-layer"></g>

                <!-- Cart / Load Box moving along hypotenuse -->
                <g id="incline-cart-group" style="cursor: grab;">
                  <!-- Dynamic cart contents rendered by InclineLab -->
                </g>
              </svg>
            </div>

            <div class="stage-quick-actions">
              <span style="font-size: 0.85rem; font-weight: 600; color: var(--text-muted);">การทดลองด่วน:</span>
              <button class="btn-quick" onclick="InclineLab.setPreset('gentle')">🛣️ ทางลาดชันน้อย (ทุ่นแรงมาก)</button>
              <button class="btn-quick" onclick="InclineLab.setPreset('steep')">⛰️ ทางลาดชันมาก (ออกแรงเยอะ)</button>
              <button class="btn-quick" onclick="InclineLab.setPreset('disabled-ramp')">♿ ทางลาดคนพิการ (สโลป 1:12)</button>
              <button class="btn-simulate-action" onclick="InclineLab.simulatePushAnimation()">▶️ ลองเข็นขึ้นยอดทางลาด</button>
            </div>
          </div>

          <!-- Controls Side Panel -->
          <div class="side-controls-panel">
            
            <!-- Height & Length Sliders -->
            <div class="control-group-card" style="border-top: 4px solid #7c3aed;">
              <div class="control-group-title">
                <span style="color: #6d28d9; font-weight: 700;">📐 สัดส่วนของทางลาด</span>
              </div>
              
              <!-- Height slider -->
              <div class="slider-row">
                <div class="slider-label-row">
                  <span>ความสูงของแท่น (h)</span>
                  <span id="val-incline-height" class="slider-val-tag" style="color: #6d28d9;">1.2 เมตร</span>
                </div>
                <input type="range" id="slider-incline-height" min="0.5" max="2.4" step="0.1" value="1.2" oninput="InclineLab.onControlChange()">
              </div>

              <!-- Length slider -->
              <div class="slider-row">
                <div class="slider-label-row">
                  <span>ความยาวทางลาด (L)</span>
                  <span id="val-incline-length" class="slider-val-tag" style="color: #6d28d9;">3.6 เมตร</span>
                </div>
                <input type="range" id="slider-incline-length" min="1.5" max="6.0" step="0.1" value="3.6" oninput="InclineLab.onControlChange()">
                <div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 0.2rem;">
                  ความชัน: <span id="tag-incline-angle" style="font-weight: 700; color: #6d28d9;">19.5°</span> (สัดส่วน h/L = <span id="tag-incline-ratio">1:3</span>)
                </div>
              </div>
            </div>

            <!-- Load Weight Slider -->
            <div class="control-group-card" style="border-top: 4px solid #3b82f6;">
              <div class="control-group-title">
                <span style="color: #1d4ed8; font-weight: 700;">📦 น้ำหนักวัตถุ (W)</span>
                <span id="tag-incline-mass" class="slider-val-tag">60 kg (600 N)</span>
              </div>
              <div class="slider-row">
                <input type="range" id="slider-incline-mass" min="10" max="100" step="5" value="60" oninput="InclineLab.onControlChange()">
                <div class="stepper-box">
                  <button class="btn-step" onclick="InclineLab.stepMass(-10)">-10</button>
                  <button class="btn-step" onclick="InclineLab.stepMass(10)">+10</button>
                  <span style="font-size: 0.8rem; color: var(--text-muted); margin-left: auto;">ปรับได้ 10 - 100 กก.</span>
                </div>
              </div>
            </div>

            <!-- Friction Surface Switcher -->
            <div class="control-group-card" style="border-top: 4px solid #f59e0b;">
              <div class="control-group-title">
                <span style="color: #b45309; font-weight: 700;">⛸️ สภาพพื้นผิว (แรงเสียดทาน)</span>
              </div>
              <div class="pill-selector">
                <button class="pill-btn active" id="btn-fric-none" onclick="InclineLab.setFriction(0.0)">ไม่มีความฝืด</button>
                <button class="pill-btn" id="btn-fric-wheels" onclick="InclineLab.setFriction(0.05)">ล้อเลื่อน (ลื่น)</button>
                <button class="pill-btn" id="btn-fric-rough" onclick="InclineLab.setFriction(0.20)">ไม้หยาบ (ฝืด)</button>
              </div>
            </div>

          </div>
        </div>

        <!-- Metrics Dashboard -->
        <div class="metrics-grid">
          <div class="metric-card">
            <div class="metric-icon-box" style="background: #eff6ff; color: #2563eb;">🏋️</div>
            <div class="metric-info">
              <h4>ถ้ายกขึ้นตรงๆ (W)</h4>
              <div id="metric-incline-w" class="metric-value">600 N (60 kg)</div>
              <div class="metric-desc">ต้องออกแรงเต็มน้ำหนักตัวของ</div>
            </div>
          </div>
          <div class="metric-card">
            <div class="metric-icon-box" style="background: #ecfdf5; color: #059669;">🛒</div>
            <div class="metric-info">
              <h4>เข็นบนทางลาด (F)</h4>
              <div id="metric-incline-f" class="metric-value">200 N (20 kg)</div>
              <div id="metric-incline-f-desc" class="metric-desc">ทุ่นแรงได้มหาศาล!</div>
            </div>
          </div>
          <div class="metric-card">
            <div class="metric-icon-box" style="background: #fffbeb; color: #d97706;">⚡</div>
            <div class="metric-info">
              <h4>การได้เปรียบเชิงกล (M.A.)</h4>
              <div id="metric-incline-ma" class="metric-value">3.0 เท่า</div>
              <div class="metric-desc">ความยาวทางลาด ÷ ความสูง (L ÷ h)</div>
            </div>
          </div>
          <div class="metric-card">
            <div class="metric-icon-box" style="background: #fdf2f8; color: #db2777;">🔥</div>
            <div class="metric-info">
              <h4>งานที่ทำ (Work)</h4>
              <div id="metric-incline-work" class="metric-value">720 จูล</div>
              <div id="metric-incline-work-desc" class="metric-desc">แรงดัน × ระยะทางลาด (F × L)</div>
            </div>
          </div>
        </div>

        <!-- Work Conservation Banner -->
        <div class="work-conservation-card">
          <div class="work-icon">💡</div>
          <div class="work-text">
            <h4>กฎเหล็ก: "ทางยาวและชันน้อยทุ่นแรงมาก แลกกับต้องเข็นไกลขึ้น" (งานเท่าเดิม!)</h4>
            <p id="work-incline-explanation">
              ถ้ายกกล่อง 600 N ขึ้นตรงๆ สูง 1.2 ม. งานที่ทำ = 600 N × 1.2 ม. = <strong>720 จูล (J)</strong><br>
              เมื่อใช้ทางลาดยาว 3.6 ม. ออกแรงเพียง 200 N แต่ต้องเข็นไกล 3.6 ม. 
              งานที่ทำ = 200 N × 3.6 ม. = <strong>720 จูล (J) เท่ากันเป๊ะ!</strong>
            </p>
          </div>
        </div>
      </div>

      <!-- Tab Real-world (ทางลาดในชีวิตจริง) -->
      <div id="incline-tab-realworld" class="tab-content-panel">
        <div class="knowledge-box">
          <h3 class="knowledge-title">📖 ทางลาดในชีวิตประจำวันของน้องๆ ม.1</h3>
          <div class="knowledge-grid">
            <div class="knowledge-item" style="border-left-color: #2563eb;">
              <h5>1. ทางลาดสำหรับผู้พิการและรถเข็น (Wheelchair Ramp)</h5>
              <p>
                ออกแบบตามหลักวิศวกรรมให้มีความชันน้อยมาก (มาตรฐานความยาวต่อความสูง 12:1) เพื่อให้ผู้ใช้วีลแชร์สามารถใช้มือหมุนล้อเข็นตัวเองขึ้นได้โดยไม่เหนื่อยเกินไป
              </p>
            </div>
            <div class="knowledge-item" style="border-left-color: #10b981;">
              <h5>2. ถนนคดเคี้ยวขึ้นภูเขาสูง</h5>
              <p>
                ทำไมวิศวกรไม่ตัดถนนพุ่งตรงขึ้นยอดเขา? เพราะถ้าตัดตรง ถนนจะชันมากจนเครื่องยนต์รถไม่มีแรงพอ การตัดถนนคดเคี้ยวไปมาช่วยเพิ่มความยาวทางลาด (L) ทำให้รถใช้แรงขับเคลื่อนน้อยลงและขับขึ้นได้ปลอดภัย
              </p>
            </div>
            <div class="knowledge-item" style="border-left-color: #f59e0b;">
              <h5>3. ตะปูควง สกรู และสลักเกลียว (Screws)</h5>
              <p>
                สลักเกลียวและตะปูควงคือ <strong>"ทางลาดที่ถูกม้วนพันรอบแกนทรงกระบอก"</strong>! เกลียวที่ถี่ก็เหมือนทางลาดที่ยาวและชันน้อย ทำให้เวลาเราใช้ไขควงขันเข้าไปในเนื้อไม้จะทุ่นแรงได้มหาศาล
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Tab Predict -->
      <div id="incline-tab-predict" class="tab-content-panel">
        <div class="predict-box">
          <div class="predict-header"><div class="predict-icon">🔮</div><div><h3>ลองทายผลเรื่องทางลาด</h3><p>เลือกคำตอบที่คิดว่าถูกต้อง แล้วกดรันเพื่อดูของจริง</p></div></div>
          <div class="predict-scenario-card"><h4 id="incline-predict-q-title" style="color: #1e3a8a; margin-bottom: 0.5rem;"></h4><p id="incline-predict-q-desc"></p></div>
          <div class="predict-options-list" id="incline-predict-options-container"></div>
          <div style="display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
            <button id="btn-run-incline-predict" class="btn-run-prediction" disabled onclick="InclineLab.executePredictionTest()">▶️ รันดูการทดลองจริง</button>
            <button class="btn-quick" onclick="InclineLab.nextPredictionScenario()">⏭️ สถานการณ์ถัดไป</button>
          </div>
          <div id="incline-predict-result-box" class="predict-result-box"><h4 id="incline-predict-fb-title"></h4><p id="incline-predict-fb-text"></p></div>
        </div>
      </div>

      <!-- Tab Missions -->
      <div id="incline-tab-missions" class="tab-content-panel">
        <div class="missions-container">
          <div class="mission-card" id="imission-card-1">
            <div class="mission-header"><span class="mission-num-badge">ภารกิจที่ 1</span><span class="mission-star-award" id="imstar-1">⭐</span></div>
            <h4 class="mission-title">🌟 เข็นกล่องขึ้นแท่นสูง 1.0 ม.</h4>
            <p class="mission-desc">มีกล่องหนัก <strong>30 กก.</strong> ต้องเข็นขึ้นแท่นสูง <strong>1.0 เมตร</strong> โดยออกแรง <strong>ไม่เกิน 10 กก.</strong> จงปรับความยาวทางลาดให้เหมาะสม!</p>
            <div class="mission-actions"><button class="btn-apply-mission" onclick="InclineLab.loadMission(1)">🛠️ จัดฉาก</button><button class="btn-check-mission" onclick="InclineLab.checkMission(1)">✅ ตรวจสอบ</button></div>
            <div class="mission-feedback" id="imission-fb-1"></div>
          </div>
          <div class="mission-card" id="imission-card-2">
            <div class="mission-header"><span class="mission-num-badge">ภารกิจที่ 2</span><span class="mission-star-award" id="imstar-2">⭐</span></div>
            <h4 class="mission-title">🌟🌟 ขนถังน้ำมัน 60 กก. ขึ้นรถบรรทุก</h4>
            <p class="mission-desc">ท้ายรถบรรทุกสูง <strong>1.2 เมตร</strong> ถังน้ำมันหนัก <strong>60 กก.</strong> โดยคุณมีแรงดัน <strong>ไม่เกิน 15 กก.</strong> จงปรับทางลาดให้ขนขึ้นได้สำเร็จ!</p>
            <div class="mission-actions"><button class="btn-apply-mission" onclick="InclineLab.loadMission(2)">🛠️ จัดฉาก</button><button class="btn-check-mission" onclick="InclineLab.checkMission(2)">✅ ตรวจสอบ</button></div>
            <div class="mission-feedback" id="imission-fb-2"></div>
          </div>
          <div class="mission-card" id="imission-card-3">
            <div class="mission-header"><span class="mission-num-badge">ภารกิจที่ 3</span><span class="mission-star-award" id="imstar-3">⭐</span></div>
            <h4 class="mission-title">🌟🌟🌟 เอาชนะแรงเสียดทานพื้นไม้หยาบ</h4>
            <p class="mission-desc">เมื่อเปิดโหมดพื้นไม้หยาบ ลากกล่อง <strong>50 กก.</strong> ขึ้นแท่นสูง <strong>1.0 เมตร</strong> จงปรับความยาวทางลาดให้ยังคงออกแรง <strong>ไม่เกิน 25 กก.</strong> ได้!</p>
            <div class="mission-actions"><button class="btn-apply-mission" onclick="InclineLab.loadMission(3)">🛠️ จัดฉาก</button><button class="btn-check-mission" onclick="InclineLab.checkMission(3)">✅ ตรวจสอบ</button></div>
            <div class="mission-feedback" id="imission-fb-3"></div>
          </div>
        </div>
      </div>

      <!-- Tab Quiz -->
      <div id="incline-tab-quiz" class="tab-content-panel">
        <div class="quiz-container">
          <h3 style="margin-bottom: 1rem;">📝 แบบทดสอบความเข้าใจเรื่องทางลาด (4 ข้อ)</h3>
          <form id="incline-quiz-form" onsubmit="event.preventDefault(); InclineLab.submitQuiz();">
            <div class="quiz-question-item">
              <div class="quiz-q-title"><strong>ข้อ 1.</strong><span>ลักษณะของทางลาดแบบใดที่ช่วยให้เรา <strong>"ผ่อนแรงได้มากที่สุด"</strong> ในการขึ้นที่สูงเท่าเดิม?</span></div>
              <div class="quiz-choices">
                <label class="quiz-choice-label"><input type="radio" name="iq1" value="a" required><span>ก. ทางลาดที่ยาวและความชันน้อย</span></label>
                <label class="quiz-choice-label"><input type="radio" name="iq1" value="b"><span>ข. ทางลาดที่สั้นและความชันมาก</span></label>
                <label class="quiz-choice-label"><input type="radio" name="iq1" value="c"><span>ค. ทางลาดแบบขั้นบันไดหักศอก</span></label>
              </div>
              <div class="quiz-explanation" id="exp-iq1">💡 <strong>เฉลย ก:</strong> ถูกต้อง! จากสูตร F = W × (h ÷ L) ยิ่งทางลาดยาว L มากขึ้น สัดส่วน h/L จะยิ่งน้อยลง ทำให้แรง F น้อยลงมาก</div>
            </div>
            <div class="quiz-question-item">
              <div class="quiz-q-title"><strong>ข้อ 2.</strong><span>กล่องหนัก 100 N ลากขึ้นทางลาดยาว 5 เมตร สูง 1 เมตร โดยไม่มีแรงเสียดทาน ต้องออกแรงกี่นิวตัน?</span></div>
              <div class="quiz-choices">
                <label class="quiz-choice-label"><input type="radio" name="iq2" value="a" required><span>ก. 10 N</span></label>
                <label class="quiz-choice-label"><input type="radio" name="iq2" value="b"><span>ข. 20 N (เพราะ 100 N × 1/5 = 20 N)</span></label>
                <label class="quiz-choice-label"><input type="radio" name="iq2" value="c"><span>ค. 50 N</span></label>
              </div>
              <div class="quiz-explanation" id="exp-iq2">💡 <strong>เฉลย ข:</strong> ถูกต้อง! คำนวณจาก F = W × (h ÷ L) = 100 × (1 ÷ 5) = 20 N ผ่อนแรงได้ถึง 5 เท่า</div>
            </div>
            <div class="quiz-question-item">
              <div class="quiz-q-title"><strong>ข้อ 3.</strong><span>สิ่งประดิษฐ์ใดต่อไปนี้ใช้หลักการของ <strong>"ทางลาดที่ถูกม้วนเป็นเกลียว"</strong>?</span></div>
              <div class="quiz-choices">
                <label class="quiz-choice-label"><input type="radio" name="iq3" value="a" required><span>ก. ตะปูควง และ น็อตสลักเกลียว</span></label>
                <label class="quiz-choice-label"><input type="radio" name="iq3" value="b"><span>ข. คีมตัดลวด</span></label>
                <label class="quiz-choice-label"><input type="radio" name="iq3" value="c"><span>ค. ไม้บรรทัดเหล็ก</span></label>
              </div>
              <div class="quiz-explanation" id="exp-iq3">💡 <strong>เฉลย ก:</strong> ถูกต้อง! เกลียวของสกรูคือทางลาดที่ม้วนรอบแกนเพื่อทุ่นแรงในการเจาะยึด</div>
            </div>
            <div class="quiz-question-item">
              <div class="quiz-q-title"><strong>ข้อ 4.</strong><span>กฎการอนุรักษ์พลังงานบอกอะไรเราเกี่ยวกับการใช้ทางลาดที่ไม่มีแรงเสียดทาน?</span></div>
              <div class="quiz-choices">
                <label class="quiz-choice-label"><input type="radio" name="iq4" value="a" required><span>ก. ทางลาดช่วยให้เราประหยัดงานทั้งหมดได้ครึ่งหนึ่ง</span></label>
                <label class="quiz-choice-label"><input type="radio" name="iq4" value="b"><span>ข. งานที่ใช้เข็นบนทางลาดเท่ากับงานที่ยกขึ้นตรงๆ พอดีเป๊ะ (W = F × s)</span></label>
                <label class="quiz-choice-label"><input type="radio" name="iq4" value="c"><span>ค. บนทางลาดไม่ต้องทำงานเลย</span></label>
              </div>
              <div class="quiz-explanation" id="exp-iq4">💡 <strong>เฉลย ข:</strong> ถูกต้อง! ทางลาดช่วยผ่อนแรงที่ต้องออก แต่ต้องแลกกับระยะทางที่ยาวขึ้น งานยังคงเท่าเดิมเสมอ!</div>
            </div>
            <div class="quiz-footer">
              <button type="submit" class="btn-check-mission">📝 ส่งคำตอบและตรวจคะแนน</button>
              <div id="incline-quiz-summary" class="quiz-score-badge"></div>
            </div>
          </form>
        </div>
      </div>
    </section>
''')

def write_javascript(f):
    f.write('''
  </main>

  <!-- Celebration Toast -->
  <div id="toast" class="celebration-toast">
    <span style="font-size: 1.6rem;">🎉</span>
    <div>
      <div id="toast-title" style="font-family: 'Prompt'; font-weight: 700;">ยินดีด้วย!</div>
      <div id="toast-msg" style="font-size: 0.9rem; color: #cbd5e1;">คุณทำภารกิจสำเร็จแล้ว</div>
    </div>
  </div>

  <script>
    /* ==========================================================================
       Sound Synthesizer (Web Audio API)
       ========================================================================== */
    const Sound = {
      enabled: true,
      ctx: null,
      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (AudioContext) this.ctx = new AudioContext();
        }
      },
      toggle() {
        this.enabled = !this.enabled;
        const btn = document.getElementById('btn-sound-toggle');
        btn.textContent = this.enabled ? '🔊' : '🔇';
        if (this.enabled) this.playTone(523.25, 0.1, 'sine');
      },
      playTone(freq, duration = 0.15, type = 'sine') {
        if (!this.enabled) return;
        try {
          this.init();
          if (!this.ctx) return;
          if (this.ctx.state === 'suspended') this.ctx.resume();
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = type;
          osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
          gain.gain.setValueAtTime(0.15, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + duration);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start();
          osc.stop(this.ctx.currentTime + duration);
        } catch (e) {}
      },
      click() { this.playTone(600, 0.05, 'triangle'); },
      balancedDing() {
        this.playTone(523.25, 0.2, 'sine');
        setTimeout(() => this.playTone(659.25, 0.25, 'sine'), 80);
        setTimeout(() => this.playTone(783.99, 0.35, 'sine'), 160);
      },
      correctFanfare() {
        this.playTone(523.25, 0.15, 'triangle');
        setTimeout(() => this.playTone(659.25, 0.15, 'triangle'), 120);
        setTimeout(() => this.playTone(783.99, 0.18, 'triangle'), 240);
        setTimeout(() => this.playTone(1046.50, 0.4, 'sine'), 360);
      },
      wrongTone() {
        this.playTone(220, 0.2, 'sawtooth');
        setTimeout(() => this.playTone(196, 0.3, 'sawtooth'), 150);
      }
    };

    /* ==========================================================================
       App State & Star Manager
       ========================================================================== */
    const App = {
      state: {
        stars: {
          lever: { m1: false, m2: false, m3: false, quiz: false },
          pulley: { m1: false, m2: false, m3: false, quiz: false },
          incline: { m1: false, m2: false, m3: false, quiz: false },
          gears: {},
          arm: {}
        }
      },
      init() {
        this.loadProgress();
        this.updateStarUI();
      },
      loadProgress() {
        try {
          const saved = localStorage.getItem('stem_simple_machines_progress_v2');
          if (saved) this.state.stars = JSON.parse(saved);
        } catch (e) {}
      },
      saveProgress() {
        try {
          localStorage.setItem('stem_simple_machines_progress_v2', JSON.stringify(this.state.stars));
        } catch (e) {}
        this.updateStarUI();
      },
      resetProgress() {
        if (confirm('คุณต้องการรีเซ็ตดาวและความก้าวหน้าทั้งหมดเพื่อเริ่มเล่นใหม่ใช่หรือไม่?')) {
          this.state.stars = {
            lever: { m1: false, m2: false, m3: false, quiz: false },
            pulley: { m1: false, m2: false, m3: false, quiz: false },
            incline: { m1: false, m2: false, m3: false, quiz: false },
            gears: {},
            arm: {}
          };
          this.saveProgress();
          LeverLab.updateMissionsUI();
          PulleyLab.updateMissionsUI();
          InclineLab.updateMissionsUI();
          this.showToast('รีเซ็ตสำเร็จ', 'เริ่มการเดินทางครั้งใหม่ได้เลย!');
        }
      },
      awardStar(room, key) {
        if (!this.state.stars[room]) this.state.stars[room] = {};
        if (!this.state.stars[room][key]) {
          this.state.stars[room][key] = true;
          this.saveProgress();
          Sound.correctFanfare();
          this.showToast('ได้รับ 1 ดาว ⭐!', 'ยอดเยี่ยมมาก พยายามต่อไปนะ');
        }
      },
      getRoomStars(room) {
        if (!this.state.stars[room]) return 0;
        return Object.values(this.state.stars[room]).filter(Boolean).length;
      },
      getTotalStars() {
        let total = 0;
        for (let r in this.state.stars) {
          total += Object.values(this.state.stars[r]).filter(Boolean).length;
        }
        return total;
      },
      updateStarUI() {
        const total = this.getTotalStars();
        document.getElementById('global-star-count').textContent = total;
        document.getElementById('home-total-stars-text').textContent = total;
        document.getElementById('card-stars-lever').textContent = this.getRoomStars('lever');
        document.getElementById('card-stars-pulley').textContent = this.getRoomStars('pulley');
        document.getElementById('card-stars-incline').textContent = this.getRoomStars('incline');
      },
      showToast(title, msg) {
        const toast = document.getElementById('toast');
        document.getElementById('toast-title').textContent = title;
        document.getElementById('toast-msg').textContent = msg;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 3500);
      },
      navigateHome() {
        Sound.click();
        document.querySelectorAll('.view-section').forEach(el => el.classList.remove('active'));
        document.getElementById('view-home').classList.add('active');
        document.getElementById('btn-back-home').style.display = 'none';
        window.scrollTo({ top: 0, behavior: 'smooth' });
      },
      enterRoom(roomName) {
        Sound.click();
        document.querySelectorAll('.view-section').forEach(el => el.classList.remove('active'));
        const targetView = document.getElementById(`view-${roomName}`);
        if (targetView) {
          targetView.classList.add('active');
          document.getElementById('btn-back-home').style.display = 'flex';
          window.scrollTo({ top: 0, behavior: 'smooth' });
          if (roomName === 'lever') LeverLab.init();
          if (roomName === 'pulley') PulleyLab.init();
          if (roomName === 'incline') InclineLab.init();
        }
      }
    };

    /* ==========================================================================
       ROOM 1: LEVER LAB ENGINE
       ========================================================================== */
    const LeverLab = {
      scale: 70,
      originX: 380,
      groundY: 320,
      pivotHeight: 70,
      state: {
        fulcrumX: 0.0,
        massLeft: 6.0,
        distLeft: 1.0,
        massRight: 2.0,
        distRight: 3.0,
        tiltAngle: 0,
        targetAngle: 0,
        isSimulatingLift: false,
        wasBalanced: false
      },
      predictionState: {
        currentScenario: 0,
        selectedOption: null,
        scenarios: [
          {
            title: "สถานการณ์ที่ 1: ถ้าเลื่อนจุดหมุน (F) เข้าใกล้ก้อนหินหนักมากขึ้น...",
            desc: "มีก้อนหินหนัก 10 กก. วางอยู่ปลายซ้าย หากเราเลื่อนจุดหมุนให้เข้าไปอยู่ชิดก้อนหินมากขึ้นเรื่อยๆ ในการงัดก้อนหินนี้ให้ลอยขึ้น เราจะต้องออกแรงกดที่ปลายขวา... อย่างไร?",
            options: [
              "ออกแรงกดน้อยลง (คานช่วยทุ่นแรงได้มากขึ้น)",
              "ออกแรงกดมากขึ้น (หนักแรงกว่าเดิม)",
              "ออกแรงกดเท่าเดิม เพราะก้อนหินหนัก 10 กก. เท่าเดิม"
            ],
            correct: 0,
            setup: { massL: 10, distL: 0.6, massR: 2, distR: 3.0, fulcrum: -1.0 },
            explanation: "ถูกต้องเก่งมาก! เมื่อจุดหมุนอยู่ใกล้ก้อนหิน แขนของน้ำหนักจะสั้นลง ทำให้เกิดโมเมนต์ต้านน้อยลง เราจึงออกแรงกดที่ปลายยาวเพียงนิดเดียวก็สามารถงัดหินขึ้นได้ (ทุ่นแรงขึ้นมหาศาล!)"
          },
          {
            title: "สถานการณ์ที่ 2: วัตถุหนัก 6 กก. อยู่ห่างจุดหมุน 1 เมตร จะใช้ลูกตุ้ม 2 กก. ถ่วงให้สมดุล...",
            desc: "ฝั่งซ้ายมีกล่อง 6 กก. อยู่ที่ระยะ 1 เมตร ถ้าเรามีลูกตุ้มเพียง 2 กก. จะต้องวางห่างจากจุดหมุนฝั่งขวากี่เมตรจึงจะสมดุลพอดี?",
            options: [
              "วางห่าง 1 เมตร (ระยะเท่ากัน)",
              "วางห่าง 2 เมตร",
              "วางห่าง 3 เมตร (เพื่อให้ 2 × 3 = 6 เท่ากันพอดี)"
            ],
            correct: 2,
            setup: { massL: 6, distL: 1.0, massR: 2, distR: 3.0, fulcrum: 0.0 },
            explanation: "ยอดเยี่ยมมาก! จากกฎของคาน โมเมนต์ซ้าย = โมเมนต์ขวา (6 กก. × 1 ม. = 2 กก. × 3 ม. = 6 เท่ากัน) ลูกตุ้มที่เบากว่าต้องอยู่ไกลกว่าเป็น 3 เท่าตัว!"
          },
          {
            title: "สถานการณ์ที่ 3: ออกแรงน้อยลง 3 เท่า แลกกับระยะทางอย่างไร?",
            desc: "ถ้าเราตั้งคานให้ทุ่นแรง 3 เท่า (ออกแรงเพียง 1 ใน 3 ของน้ำหนัก) หากต้องการให้ก้อนของหนักลอยสูงขึ้น 10 เซนติเมตร เราจะต้องกดปลายคานด้านที่เราออกแรงลงลึกเท่าใด?",
            options: [
              "กดลงลึกเพียง 3.3 เซนติเมตร",
              "กดลงลึก 10 เซนติเมตร เท่ากัน",
              "กดลงลึกถึง 30 เซนติเมตร (ระยะทางเพิ่มขึ้น 3 เท่า)"
            ],
            correct: 2,
            setup: { massL: 9, distL: 0.8, massR: 3, distR: 2.4, fulcrum: 0.0 },
            explanation: "เป๊ะเลย! นี่คือกฎเหล็กของฟิสิกส์: งานที่ทำ = แรง × ระยะทาง (W = F × s) เมื่อได้แรงเพิ่ม 3 เท่า เราต้องจ่ายคืนด้วยระยะทางที่ต้องกดเพิ่มขึ้น 3 เท่าเช่นกัน งานจึงเท่าเดิมเสมอ!"
          }
        ]
      },
      init() {
        this.renderScaleTicks();
        this.setupDragging();
        this.onControlChange();
        this.showClass(1);
        this.loadPredictionScenario(0);
        this.updateMissionsUI();
        if (!this.loopRunning) {
          this.loopRunning = true;
          this.renderLoop();
        }
      },
      renderScaleTicks() {
        const groundTicks = document.getElementById('ground-ticks');
        const beamTicks = document.getElementById('beam-ticks');
        groundTicks.innerHTML = '';
        beamTicks.innerHTML = '';
        for (let m = -4; m <= 4; m += 0.5) {
          const x = this.originX + m * this.scale;
          const isMajor = Number.isInteger(m);
          const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
          line.setAttribute('x1', x); line.setAttribute('y1', this.groundY);
          line.setAttribute('x2', x); line.setAttribute('y2', this.groundY + (isMajor ? 12 : 6));
          line.setAttribute('stroke', '#94a3b8');
          groundTicks.appendChild(line);
          if (isMajor && m !== 0) {
            const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            txt.setAttribute('x', x); txt.setAttribute('y', this.groundY + 24);
            txt.setAttribute('fill', '#64748b'); txt.setAttribute('font-size', '10');
            txt.setAttribute('font-family', 'Prompt'); txt.setAttribute('text-anchor', 'middle');
            txt.textContent = `${Math.abs(m)}m`;
            groundTicks.appendChild(txt);
          }
        }
        for (let m = -4; m <= 4; m += 0.5) {
          const x = m * this.scale;
          const isMajor = Number.isInteger(m);
          const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
          line.setAttribute('x1', x); line.setAttribute('y1', -12);
          line.setAttribute('x2', x); line.setAttribute('y2', -12 + (isMajor ? 8 : 4));
          line.setAttribute('stroke', '#ffffff'); line.setAttribute('opacity', '0.7');
          beamTicks.appendChild(line);
        }
      },
      switchTab(tabId) {
        Sound.click();
        const tabBtns = document.querySelectorAll('#view-lever .tab-btn');
        const tabPanels = document.querySelectorAll('#view-lever .tab-content-panel');
        tabBtns.forEach(btn => btn.classList.remove('active'));
        tabPanels.forEach(p => p.classList.remove('active'));
        const targetTab = document.getElementById(`lever-tab-${tabId}`);
        if (targetTab) targetTab.classList.add('active');
        const map = { explore: 0, classes: 1, predict: 2, missions: 3, quiz: 4 };
        if (tabBtns[map[tabId]]) tabBtns[map[tabId]].classList.add('active');
      },
      stepValue(field, step) {
        Sound.click();
        const el = document.getElementById(`slider-${field}`);
        el.value = Math.max(1, Math.min(20, parseFloat(el.value) + step));
        this.onControlChange();
      },
      onControlChange() {
        this.state.massLeft = parseFloat(document.getElementById('slider-mass-left').value);
        this.state.distLeft = parseFloat(document.getElementById('slider-dist-left').value);
        this.state.massRight = parseFloat(document.getElementById('slider-mass-right').value);
        this.state.distRight = parseFloat(document.getElementById('slider-dist-right').value);
        this.state.fulcrumX = parseFloat(document.getElementById('slider-fulcrum').value);
        this.updatePhysicsAndUI();
      },
      updatePhysicsAndUI() {
        const { massLeft, distLeft, massRight, distRight, fulcrumX } = this.state;
        const forceLeft = massLeft * 10;
        const forceRight = massRight * 10;
        const momentLeft = forceLeft * distLeft;
        const momentRight = forceRight * distRight;
        const torqueDiff = momentRight - momentLeft;
        const ma = (distRight / distLeft).toFixed(2);

        document.getElementById('val-mass-left').textContent = `${massLeft} kg (${forceLeft} N)`;
        document.getElementById('val-dist-left').textContent = `${distLeft.toFixed(1)} m`;
        document.getElementById('val-mass-right').textContent = `${massRight} kg (${forceRight} N)`;
        document.getElementById('val-dist-right').textContent = `${distRight.toFixed(1)} m`;
        document.getElementById('val-fulcrum-pos').textContent = fulcrumX === 0 ? "กึ่งกลาง (0.0 m)" : `${fulcrumX > 0 ? '+' : ''}${fulcrumX.toFixed(1)} m`;

        document.getElementById('tag-m-left').textContent = `M = ${momentLeft.toFixed(0)} N·m`;
        document.getElementById('tag-m-right').textContent = `M = ${momentRight.toFixed(0)} N·m`;

        document.getElementById('left-mass-text').textContent = `${massLeft} kg`;
        document.getElementById('left-force-text').textContent = `(${forceLeft} N)`;
        document.getElementById('right-mass-text').textContent = `${massRight} kg`;
        document.getElementById('right-force-text').textContent = `(${forceRight} N)`;

        document.getElementById('metric-left-torque').textContent = `${momentLeft.toFixed(0)} N·m`;
        document.getElementById('metric-right-torque').textContent = `${momentRight.toFixed(0)} N·m`;
        document.getElementById('metric-ma').textContent = `${ma} เท่า`;
        document.getElementById('metric-ma-desc').textContent = distRight >= distLeft ? `ทุ่นแรงได้ ${ma} เท่า!` : `ไม่ทุ่นแรง (ได้ระยะทาง)`;
        document.getElementById('metric-torque-diff').textContent = `${Math.abs(torqueDiff).toFixed(1)} N·m`;

        const isBalanced = Math.abs(torqueDiff) < 1.0;
        const badge = document.getElementById('lever-balance-badge');
        const summaryText = document.getElementById('metric-balance-summary');
        const diffIcon = document.getElementById('metric-diff-icon');

        if (isBalanced) {
          badge.className = 'balance-status-badge balanced';
          badge.innerHTML = '<span>⚖️</span> <span>คานอยู่ในสภาวะสมดุลพอดี!</span>';
          summaryText.textContent = 'สมดุลพอดี! โมเมนต์ทวน = โมเมนต์ตาม';
          diffIcon.style.color = '#10b981';
          this.state.targetAngle = 0;
          if (!this.state.wasBalanced) {
            Sound.balancedDing();
            this.state.wasBalanced = true;
          }
        } else if (torqueDiff < 0) {
          badge.className = 'balance-status-badge tilted-left';
          badge.innerHTML = '<span>↖️</span> <span>คานเอียงไปทางซ้าย</span>';
          summaryText.textContent = `เอียงซ้าย โมเมนต์ทวนมากกว่า ${Math.abs(torqueDiff).toFixed(0)} N·m`;
          diffIcon.style.color = '#3b82f6';
          this.state.targetAngle = Math.max(-12, (torqueDiff / 30) * 12);
          this.state.wasBalanced = false;
        } else {
          badge.className = 'balance-status-badge tilted-right';
          badge.innerHTML = '<span>↘️</span> <span>คานเอียงไปทางขวา</span>';
          summaryText.textContent = `เอียงขวา โมเมนต์ตามมากกว่า ${torqueDiff.toFixed(0)} N·m`;
          diffIcon.style.color = '#f59e0b';
          this.state.targetAngle = Math.min(12, (torqueDiff / 30) * 12);
          this.state.wasBalanced = false;
        }

        const liftHeight = 0.20;
        const effortDistance = liftHeight * (distRight / distLeft);
        const workJoules = forceLeft * liftHeight;
        document.getElementById('work-explanation-text').innerHTML = `
          ถ้ายกกล่องซ้ายขึ้นสูง <strong>${liftHeight.toFixed(2)} ม.</strong> 
          ต้องออกแรงกดฝั่งขวาลงลึก <strong>${effortDistance.toFixed(2)} ม.</strong> 
          โดยงานที่ทำทั้งสองฝั่งเท่ากันคือ <strong>${workJoules.toFixed(1)} จูล (J)</strong> พอดีเป๊ะ!
        `;
        this.updateSvgGeometry();
      },
      updateSvgGeometry() {
        const fulcrumScreenX = this.originX + (this.state.fulcrumX * this.scale);
        const fulcrumScreenY = this.groundY - this.pivotHeight;
        document.getElementById('fulcrum-group').setAttribute('transform', `translate(${fulcrumScreenX}, ${fulcrumScreenY})`);
        document.getElementById('beam-rotating-group').setAttribute('transform', `translate(${fulcrumScreenX}, ${fulcrumScreenY}) rotate(${this.state.tiltAngle})`);
        document.getElementById('main-beam').setAttribute('x', -this.state.fulcrumX * this.scale - 320);

        const leftScreenX = -this.state.distLeft * this.scale;
        document.getElementById('left-weight-group').setAttribute('transform', `translate(${leftScreenX}, 0)`);
        const leftBoxSize = 45 + (this.state.massLeft * 1.8);
        const leftBox = document.getElementById('left-box');
        leftBox.setAttribute('width', leftBoxSize); leftBox.setAttribute('height', leftBoxSize);
        leftBox.setAttribute('x', -leftBoxSize / 2);

        const rightScreenX = this.state.distRight * this.scale;
        document.getElementById('right-weight-group').setAttribute('transform', `translate(${rightScreenX}, 0)`);
        const rightBoxSize = 45 + (this.state.massRight * 1.8);
        const rightBox = document.getElementById('right-box');
        rightBox.setAttribute('width', rightBoxSize); rightBox.setAttribute('height', rightBoxSize);
        rightBox.setAttribute('x', -rightBoxSize / 2);
      },
      renderLoop() {
        if (!LeverLab.state.isSimulatingLift) {
          const diff = LeverLab.state.targetAngle - LeverLab.state.tiltAngle;
          LeverLab.state.tiltAngle += diff * 0.12;
        }
        LeverLab.updateSvgGeometry();
        requestAnimationFrame(() => LeverLab.renderLoop());
      },
      simulateLiftAnimation() {
        if (this.state.isSimulatingLift) return;
        this.state.isSimulatingLift = true;
        Sound.click();
        const initialAngle = this.state.tiltAngle;
        const targetLiftAngle = 10;
        let step = 0;
        const animInterval = setInterval(() => {
          step++;
          if (step <= 25) {
            this.state.tiltAngle = initialAngle + (targetLiftAngle - initialAngle) * (step / 25);
          } else if (step <= 40) {
          } else if (step <= 65) {
            this.state.tiltAngle = targetLiftAngle - (targetLiftAngle - this.state.targetAngle) * ((step - 40) / 25);
          } else {
            clearInterval(animInterval);
            this.state.isSimulatingLift = false;
          }
        }, 30);
      },
      setupDragging() {
        const svg = document.getElementById('lever-svg');
        let activeDrag = null;
        const getSvgCoords = (e) => {
          const pt = svg.createSVGPoint();
          if (e.touches && e.touches.length > 0) {
            pt.x = e.touches[0].clientX; pt.y = e.touches[0].clientY;
          } else {
            pt.x = e.clientX; pt.y = e.clientY;
          }
          return pt.matrixTransform(svg.getScreenCTM().inverse());
        };
        const onStartDrag = (type, e) => { e.preventDefault(); activeDrag = type; Sound.click(); };
        document.getElementById('left-weight-group').addEventListener('mousedown', (e) => onStartDrag('left', e));
        document.getElementById('left-weight-group').addEventListener('touchstart', (e) => onStartDrag('left', e), { passive: false });
        document.getElementById('right-weight-group').addEventListener('mousedown', (e) => onStartDrag('right', e));
        document.getElementById('right-weight-group').addEventListener('touchstart', (e) => onStartDrag('right', e), { passive: false });
        document.getElementById('fulcrum-group').addEventListener('mousedown', (e) => onStartDrag('fulcrum', e));
        document.getElementById('fulcrum-group').addEventListener('touchstart', (e) => onStartDrag('fulcrum', e), { passive: false });

        const onMove = (e) => {
          if (!activeDrag) return;
          e.preventDefault();
          const coords = getSvgCoords(e);
          const fulcrumScreenX = this.originX + (this.state.fulcrumX * this.scale);
          if (activeDrag === 'left') {
            const distPx = fulcrumScreenX - coords.x;
            const distM = Math.max(0.2, Math.min(3.0, distPx / this.scale));
            document.getElementById('slider-dist-left').value = distM.toFixed(1);
            this.onControlChange();
          } else if (activeDrag === 'right') {
            const distPx = coords.x - fulcrumScreenX;
            const distM = Math.max(0.2, Math.min(3.0, distPx / this.scale));
            document.getElementById('slider-dist-right').value = distM.toFixed(1);
            this.onControlChange();
          } else if (activeDrag === 'fulcrum') {
            const offsetPx = coords.x - this.originX;
            const offsetM = Math.max(-1.5, Math.min(1.5, offsetPx / this.scale));
            document.getElementById('slider-fulcrum').value = offsetM.toFixed(1);
            this.onControlChange();
          }
        };
        const onEnd = () => { if (activeDrag) activeDrag = null; };
        window.addEventListener('mousemove', onMove);
        window.addEventListener('touchmove', onMove, { passive: false });
        window.addEventListener('mouseup', onEnd);
        window.addEventListener('touchend', onEnd);
      },
      applyPreset(type) {
        Sound.click();
        if (type === 'seesaw') {
          document.getElementById('slider-mass-left').value = 5;
          document.getElementById('slider-dist-left').value = 2.0;
          document.getElementById('slider-mass-right').value = 5;
          document.getElementById('slider-dist-right').value = 2.0;
          document.getElementById('slider-fulcrum').value = 0.0;
        } else if (type === 'heavy-rock') {
          document.getElementById('slider-mass-left').value = 12;
          document.getElementById('slider-dist-left').value = 0.6;
          document.getElementById('slider-mass-right').value = 3;
          document.getElementById('slider-dist-right').value = 2.4;
          document.getElementById('slider-fulcrum').value = 0.0;
        } else if (type === 'balanced-diff') {
          document.getElementById('slider-mass-left').value = 6;
          document.getElementById('slider-dist-left').value = 1.0;
          document.getElementById('slider-mass-right').value = 2;
          document.getElementById('slider-dist-right').value = 3.0;
          document.getElementById('slider-fulcrum').value = 0.0;
        }
        this.onControlChange();
      },
      showClass(classNum) {
        const container = document.getElementById('class-detail-view');
        if (classNum === 1) {
          container.innerHTML = `
            <h4 style="color: #1e3a8a; margin-bottom: 0.4rem;">🥇 คานอันดับ 1: จุดหมุน (F) อยู่ตรงกลาง</h4>
            <p style="color: #475569; margin-bottom: 0.5rem;">ผ่อนแรงหรือไม่ผ่อนแรงก็ได้ เช่น <strong>กรรไกร, ไม้กระดก, ชะแลงงัดหิน</strong></p>
          `;
        } else if (classNum === 2) {
          container.innerHTML = `
            <h4 style="color: #065f46; margin-bottom: 0.4rem;">🥈 คานอันดับ 2: น้ำหนัก (W) อยู่ตรงกลาง</h4>
            <p style="color: #475569; margin-bottom: 0.5rem;"><strong>ทุ่นแรงเสมอ (M.A. > 1)!</strong> เช่น <strong>รถเข็นทราย, ที่เปิดขวด, ที่ตัดกระดาษ</strong></p>
          `;
        } else if (classNum === 3) {
          container.innerHTML = `
            <h4 style="color: #7c3aed; margin-bottom: 0.4rem;">🥉 คานอันดับ 3: แรงพยายาม (E) อยู่ตรงกลาง</h4>
            <p style="color: #475569; margin-bottom: 0.5rem;">ไม่ทุ่นแรง แต่ว่องไวและได้ระยะ เช่น <strong>ตะเกียบ, คีมคีบน้ำแข็ง, แขนมนุษย์</strong></p>
          `;
        }
      },
      loadPredictionScenario(idx) {
        this.predictionState.currentScenario = idx;
        const sc = this.predictionState.scenarios[idx];
        document.getElementById('predict-question-title').textContent = sc.title;
        document.getElementById('predict-question-desc').textContent = sc.desc;
        const container = document.getElementById('predict-options-container');
        container.innerHTML = '';
        sc.options.forEach((optText, i) => {
          const letter = ['ก', 'ข', 'ค'][i];
          const btn = document.createElement('button');
          btn.className = 'predict-option-btn';
          btn.onclick = () => this.selectPredictionOption(i);
          btn.innerHTML = `<span class="opt-badge">${letter}</span><span>${optText}</span>`;
          container.appendChild(btn);
        });
        document.getElementById('btn-run-prediction').disabled = true;
        document.getElementById('predict-result-box').style.display = 'none';
      },
      selectPredictionOption(index) {
        Sound.click();
        this.predictionState.selectedOption = index;
        const btns = document.querySelectorAll('#predict-options-container .predict-option-btn');
        btns.forEach((b, i) => {
          if (i === index) b.classList.add('selected'); else b.classList.remove('selected');
        });
        document.getElementById('btn-run-prediction').disabled = false;
      },
      executePredictionTest() {
        const sc = this.predictionState.scenarios[this.predictionState.currentScenario];
        const isCorrect = this.predictionState.selectedOption === sc.correct;
        document.getElementById('slider-mass-left').value = sc.setup.massL;
        document.getElementById('slider-dist-left').value = sc.setup.distL;
        document.getElementById('slider-mass-right').value = sc.setup.massR;
        document.getElementById('slider-dist-right').value = sc.setup.distR;
        document.getElementById('slider-fulcrum').value = sc.setup.fulcrum;
        this.onControlChange();

        const fbBox = document.getElementById('predict-result-box');
        fbBox.style.display = 'block';
        if (isCorrect) {
          Sound.correctFanfare();
          fbBox.className = 'predict-result-box correct';
          document.getElementById('predict-feedback-title').innerHTML = '🎉 ถูกต้องแม่นยำ!';
          document.getElementById('predict-feedback-text').innerHTML = sc.explanation;
        } else {
          Sound.wrongTone();
          fbBox.className = 'predict-result-box incorrect';
          document.getElementById('predict-feedback-title').innerHTML = '🧐 ผลการทดลองจริงเป็นอีกแบบหนึ่ง ลองสังเกตดูสิ!';
          document.getElementById('predict-feedback-text').innerHTML = `${sc.explanation} (สังเกตผลการจำลองบนคานจริง)`;
        }
      },
      nextPredictionScenario() {
        Sound.click();
        const next = (this.predictionState.currentScenario + 1) % this.predictionState.scenarios.length;
        this.loadPredictionScenario(next);
      },
      loadMission(num) {
        Sound.click();
        this.switchTab('explore');
        if (num === 1) {
          document.getElementById('slider-mass-left').value = 6;
          document.getElementById('slider-dist-left').value = 1.0;
          document.getElementById('slider-mass-right').value = 2;
          document.getElementById('slider-dist-right').value = 1.0;
          document.getElementById('slider-fulcrum').value = 0.0;
        } else if (num === 2) {
          document.getElementById('slider-mass-left').value = 12;
          document.getElementById('slider-dist-left').value = 0.5;
          document.getElementById('slider-mass-right').value = 4;
          document.getElementById('slider-dist-right').value = 1.0;
          document.getElementById('slider-fulcrum').value = 0.0;
        } else if (num === 3) {
          document.getElementById('slider-mass-left').value = 18;
          document.getElementById('slider-dist-left').value = 0.8;
          document.getElementById('slider-mass-right').value = 2;
          document.getElementById('slider-dist-right').value = 2.4;
          document.getElementById('slider-fulcrum').value = 0.0;
        }
        this.onControlChange();
      },
      checkMission(num) {
        const { massLeft, distLeft, massRight, distRight } = this.state;
        const momentL = massLeft * distLeft;
        const momentR = massRight * distRight;
        const isBalanced = Math.abs(momentL - momentR) < 0.2;
        const fb = document.getElementById(`mission-fb-${num}`);
        fb.style.display = 'block';

        if (num === 1) {
          if (massLeft === 6 && Math.abs(distLeft - 1.0) < 0.15 && massRight === 2 && Math.abs(distRight - 3.0) < 0.15 && isBalanced) {
            fb.style.color = '#059669';
            fb.textContent = '🎉 ยอดเยี่ยมมาก! คานสมดุลพอดี (6 × 1 = 2 × 3 = 6) ได้รับ 1 ดาว ⭐';
            App.awardStar('lever', 'm1');
            this.updateMissionsUI();
          } else {
            Sound.wrongTone();
            fb.style.color = '#dc2626';
            fb.textContent = `ยังไม่สมดุลนะ! โมเมนต์ซ้าย = ${momentL.toFixed(1)} โมเมนต์ขวา = ${momentR.toFixed(1)} ลองเลื่อนลูกตุ้ม 2 กก. ไปที่ระยะ 3.0 ม. ดูสิ`;
          }
        } else if (num === 2) {
          if (massLeft === 12 && Math.abs(distLeft - 0.5) < 0.15 && massRight <= 3 && isBalanced) {
            fb.style.color = '#059669';
            fb.textContent = `🎉 สำเร็จแล้ว! คุณใช้แรงเพียง ${massRight} กก. งัดหิน 12 กก. ได้สำเร็จ ทุ่นแรงได้ ${(12/massRight).toFixed(1)} เท่า!`;
            App.awardStar('lever', 'm2');
            this.updateMissionsUI();
          } else {
            Sound.wrongTone();
            fb.style.color = '#dc2626';
            fb.textContent = `ยังไม่ผ่านนะ! ต้องใช้แรงไม่เกิน 3 กก. และปรับให้คานสมดุลพอดี`;
          }
        } else if (num === 3) {
          if (Math.abs(momentL - 14.4) < 0.5 && Math.abs(distRight - 2.4) < 0.15 && massRight === 6 && isBalanced) {
            fb.style.color = '#059669';
            fb.textContent = '🎉 สุดยอดนักคำนวณ! ออกแรงเพียง 6 กก. ที่ระยะ 2.4 ม. ก็ยกดิน 18 กก. ได้สบาย';
            App.awardStar('lever', 'm3');
            this.updateMissionsUI();
          } else {
            Sound.wrongTone();
            fb.style.color = '#dc2626';
            fb.textContent = `ยังไม่ถูกต้องนะ! 18 กก. × 0.8 ม. = 14.4 ดังนั้นที่ระยะ 2.4 ม. ต้องออกแรง 14.4 ÷ 2.4 = 6 กิโลกรัม`;
          }
        }
      },
      updateMissionsUI() {
        const stars = App.state.stars.lever || {};
        ['m1', 'm2', 'm3'].forEach((mKey, idx) => {
          const num = idx + 1;
          const card = document.getElementById(`mission-card-${num}`);
          const starIcon = document.getElementById(`mstar-${num}`);
          if (stars[mKey]) {
            card.classList.add('completed');
            starIcon.textContent = '⭐ ได้รับแล้ว!';
          } else {
            card.classList.remove('completed');
            starIcon.textContent = '⭐';
          }
        });
      },
      submitQuiz() {
        Sound.click();
        const form = document.getElementById('lever-quiz-form');
        const answers = { lq1: 'b', lq2: 'a', lq3: 'a', lq4: 'a' };
        let score = 0;
        ['lq1', 'lq2', 'lq3', 'lq4'].forEach(q => {
          const selected = form.elements[q].value;
          document.getElementById(`exp-${q}`).style.display = 'block';
          form.querySelectorAll(`input[name="${q}"]`).forEach(r => {
            const lbl = r.parentElement;
            lbl.classList.remove('correct-answer', 'wrong-answer');
            if (r.value === answers[q]) lbl.classList.add('correct-answer');
            else if (r.checked && r.value !== answers[q]) lbl.classList.add('wrong-answer');
          });
          if (selected === answers[q]) score++;
        });
        const summary = document.getElementById('lever-quiz-summary');
        summary.innerHTML = `ได้คะแนน: ${score} / 4 คะแนน`;
        if (score === 4) {
          Sound.correctFanfare();
          summary.innerHTML += ` 🎉 รับดาวควิซไปเลย ⭐`;
          App.awardStar('lever', 'quiz');
        } else {
          Sound.wrongTone();
        }
      }
    };

    /* ==========================================================================
       ROOM 2: PULLEY LAB ENGINE (ห้องปฏิบัติการรอก)
       ========================================================================== */
    const PulleyLab = {
      state: {
        type: 'fixed', // 'fixed' | 'movable' | 'compound'
        strands: 4,    // for compound: 2 to 6
        mass: 60,      // kg
        liftHeight: 0.60, // meters (0 to 1.6m)
        isSimulating: false
      },
      predictionState: {
        currentScenario: 0,
        selectedOption: null,
        scenarios: [
          {
            title: "สถานการณ์ที่ 1: ยกถังน้ำ 20 กก. ด้วยรอกเดี่ยวตายตัว (Fixed Pulley)...",
            desc: "หากมีถังน้ำหนัก 20 กก. คล้องเชือกผ่านรอกเดี่ยวตายตัวที่ติดอยู่กับเพดาน เราจะต้องออกแรงดึงเชือกกี่กิโลกรัม?",
            options: [
              "ออกแรงเพียง 10 กิโลกรัม (ทุ่นแรงครึ่งหนึ่ง)",
              "ออกแรง 20 กิโลกรัม เท่ากับน้ำหนักถังน้ำ",
              "ออกแรง 40 กิโลกรัม เพราะมีแรงเสียดทานของรอก"
            ],
            correct: 1,
            setup: { type: 'fixed', strands: 1, mass: 20 },
            explanation: "ถูกต้อง! รอกเดี่ยวตายตัว M.A. = 1 ไม่ช่วยผ่อนแรงเลย เราต้องออกแรง 20 กก. เท่าเดิม แต่มีประโยชน์คือช่วยเปลี่ยนทิศทางแรง ให้เราดึงลงตามแรงโน้มถ่วงได้สะดวกขึ้น"
          },
          {
            title: "สถานการณ์ที่ 2: เปลี่ยนมาใช้รอกเดี่ยวเคลื่อนที่ (Movable Pulley)...",
            desc: "ถ้านำรอกมาแขวนไว้กับตัวกล่อง 40 กก. (ปลายเชือกข้างหนึ่งยึดเพดาน อีกข้างหนึ่งดึงขึ้น) เราจะออกแรงดึงเชือกเท่าใด?",
            options: [
              "ออกแรง 20 กิโลกรัม (ทุ่นแรงได้ครึ่งหนึ่ง)",
              "ออกแรง 40 กิโลกรัม เท่าเดิม",
              "ออกแรง 80 กิโลกรัม"
            ],
            correct: 0,
            setup: { type: 'movable', strands: 2, mass: 40 },
            explanation: "ยอดเยี่ยมมาก! รอกเดี่ยวเคลื่อนที่มีเชือก 2 เส้นช่วยกันหิ้วน้ำหนักของกล่อง เราจึงออกแรงเพียงครึ่งเดียว F = 40 ÷ 2 = 20 กก. ทุ่นแรงได้ 2 เท่า!"
          },
          {
            title: "สถานการณ์ที่ 3: ใช้รอกพวง 4 เส้น ยกของสูง 1.0 เมตร ต้องดึงเชือกยาวเท่าใด?",
            desc: "ใช้รอกพวงที่มีเชือกรับน้ำหนัก 4 เส้น (ทุ่นแรง 4 เท่า ออกแรงเพียง 1 ใน 4) ถ้ายกของสูงขึ้น 1.0 เมตร เราจะต้องสาวเชือกยาวกี่เมตร?",
            options: [
              "สาวเชือกยาว 0.25 เมตร (สั้นลง)",
              "สาวเชือกยาว 1.0 เมตร เท่ากับความสูง",
              "สาวเชือกยาว 4.0 เมตร (ยาวขึ้น 4 เท่าตามจำนวนเชือก)"
            ],
            correct: 2,
            setup: { type: 'compound', strands: 4, mass: 60 },
            explanation: "แม่นยำมาก! ตามกฎการอนุรักษ์พลังงาน (งาน = แรง × ระยะทาง) เมื่อเราได้แรงเพิ่ม 4 เท่า เราต้องแลกด้วยระยะทางดึงเชือกที่ยาวขึ้น 4 เท่าตัว (s = 4 × 1.0 = 4.0 ม.) งานจึงเท่าเดิมเสมอ!"
          }
        ]
      },
      init() {
        this.setupDragging();
        this.setType(this.state.type);
        this.onControlChange();
        this.loadPredictionScenario(0);
        this.updateMissionsUI();
      },
      switchTab(tabId) {
        Sound.click();
        const tabBtns = document.querySelectorAll('#view-pulley .tab-btn');
        const tabPanels = document.querySelectorAll('#view-pulley .tab-content-panel');
        tabBtns.forEach(btn => btn.classList.remove('active'));
        tabPanels.forEach(p => p.classList.remove('active'));
        const targetTab = document.getElementById(`pulley-tab-${tabId}`);
        if (targetTab) targetTab.classList.add('active');
        const map = { explore: 0, types: 1, predict: 2, missions: 3, quiz: 4 };
        if (tabBtns[map[tabId]]) tabBtns[map[tabId]].classList.add('active');
      },
      setType(t) {
        Sound.click();
        this.state.type = t;
        document.querySelectorAll('.pill-selector button').forEach(b => b.classList.remove('active'));
        document.getElementById(`btn-ptype-${t}`).classList.add('active');
        const strandRow = document.getElementById('compound-strand-row');
        strandRow.style.display = (t === 'compound') ? 'block' : 'none';
        this.onControlChange();
      },
      onStrandChange() {
        this.state.strands = parseInt(document.getElementById('slider-pulley-strands').value);
        document.getElementById('val-pulley-strands').textContent = `${this.state.strands} เส้น`;
        this.onControlChange();
      },
      stepMass(delta) {
        Sound.click();
        const el = document.getElementById('slider-pulley-mass');
        el.value = Math.max(10, Math.min(100, parseInt(el.value) + delta));
        this.onControlChange();
      },
      onControlChange() {
        this.state.mass = parseFloat(document.getElementById('slider-pulley-mass').value);
        this.state.liftHeight = parseFloat(document.getElementById('slider-pulley-height').value);
        this.updatePhysicsAndUI();
      },
      updatePhysicsAndUI() {
        const { type, strands, mass, liftHeight } = this.state;
        const weightN = mass * 10;
        let n = 1;
        if (type === 'fixed') n = 1;
        else if (type === 'movable') n = 2;
        else if (type === 'compound') n = strands;

        const forceN = weightN / n;
        const forceKg = mass / n;
        const ropeDistance = liftHeight * n;
        const workJoules = weightN * liftHeight;

        // Update Labels
        document.getElementById('tag-pulley-weight').textContent = `${mass} kg (${weightN} N)`;
        document.getElementById('tag-pulley-height').textContent = `${liftHeight.toFixed(2)} ม.`;
        document.getElementById('metric-pulley-w').textContent = `${mass} kg`;
        document.getElementById('metric-pulley-w-desc').textContent = `แรงโน้มถ่วง = ${weightN} N`;

        document.getElementById('metric-pulley-f').textContent = `${forceKg.toFixed(1)} kg (${forceN.toFixed(0)} N)`;
        document.getElementById('metric-pulley-f-desc').textContent = n > 1 ? `ทุ่นแรงได้ ${n} เท่า!` : `ไม่ทุ่นแรง (เปลี่ยนทิศทาง)`;

        document.getElementById('metric-pulley-ma').textContent = `${n}.0 เท่า`;
        document.getElementById('metric-pulley-ma-desc').textContent = n === 1 ? 'รอกเดี่ยวตายตัว (M.A. = 1)' : `มีเชือก ${n} เส้นช่วยพยุงน้ำหนัก`;

        document.getElementById('metric-pulley-s').textContent = `${ropeDistance.toFixed(2)} ม.`;
        document.getElementById('metric-pulley-s-desc').textContent = `ระยะดึง = ${liftHeight.toFixed(2)} ม. × ${n}`;

        document.getElementById('work-pulley-explanation').innerHTML = `
          ในการยกกล่อง <strong>${weightN} N</strong> สูง <strong>${liftHeight.toFixed(2)} ม.</strong> งานที่ได้ = <strong>${workJoules.toFixed(0)} จูล (J)</strong><br>
          ${n > 1 ? `เมื่อมีเชือกรับน้ำหนัก ${n} เส้น ออกแรงดึงเพียง ${forceN.toFixed(0)} N แต่ต้องดึงเชือกยาว ${ropeDistance.toFixed(2)} ม.` : `ดึงเชือกด้วยแรง ${forceN.toFixed(0)} N เป็นระยะทาง ${ropeDistance.toFixed(2)} ม.`} 
          งานที่ทำ = ${forceN.toFixed(0)} N × ${ropeDistance.toFixed(2)} ม. = <strong>${workJoules.toFixed(0)} จูล (J) เท่ากันเป๊ะ!</strong>
        `;

        this.renderSvg(n, liftHeight, forceKg);
      },
      renderSvg(n, h, forceKg) {
        const layer = document.getElementById('pulley-dynamic-layer');
        const scaleLayer = document.getElementById('pulley-scale-layer');
        layer.innerHTML = '';
        scaleLayer.innerHTML = '';

        const maxH = 1.6;
        const groundY = 320;
        const ceilingY = 34;
        const boxH = 55;
        const boxW = 75;
        const travelPx = 130;
        const currentLiftPx = (h / maxH) * travelPx;
        const loadBoxY = groundY - boxH - currentLiftPx;

        if (this.state.type === 'fixed') {
          // 1 Fixed Pulley at ceiling
          const px = 380, py = 75, r = 24;
          const ropeLeftX = px - r;
          const ropeRightX = px + r;
          const handY = 120 + currentLiftPx;

          let html = `
            <!-- Bracket to ceiling -->
            <rect x="${px - 4}" y="${ceilingY}" width="8" height="${py - ceilingY}" fill="#64748b" />
            <!-- Pulley wheel -->
            <circle cx="${px}" cy="${py}" r="${r}" fill="url(#pulley-metal)" stroke="#334155" stroke-width="2.5" />
            <circle cx="${px}" cy="${py}" r="5" fill="#ef4444" />
            <!-- Left Rope to Load Box -->
            <line x1="${ropeLeftX}" y1="${py}" x2="${ropeLeftX}" y2="${loadBoxY}" stroke="#d97706" stroke-width="3.5" />
            <!-- Load Box -->
            <rect x="${ropeLeftX - boxW/2}" y="${loadBoxY}" width="${boxW}" height="${boxH}" rx="6" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2" filter="url(#pulley-shadow)" />
            <text x="${ropeLeftX}" y="${loadBoxY + 30}" fill="#ffffff" font-family="Prompt" font-weight="700" font-size="14" text-anchor="middle">${this.state.mass} kg</text>
            <text x="${ropeLeftX}" y="${loadBoxY + 46}" fill="#dbeafe" font-family="Prompt" font-size="11" text-anchor="middle">(${this.state.mass * 10} N)</text>
            <!-- Pulley wrap arc -->
            <path d="M ${ropeLeftX} ${py} A ${r} ${r} 0 0 1 ${ropeRightX} ${py}" fill="none" stroke="#d97706" stroke-width="3.5" />
            <!-- Right Rope to Pull Handle -->
            <line x1="${ropeRightX}" y1="${py}" x2="${ropeRightX}" y2="${handY}" stroke="#d97706" stroke-width="3.5" />
            <!-- Pull Handle -->
            <g id="pulley-pull-handle" style="cursor: ns-resize;" transform="translate(${ropeRightX}, ${handY})">
              <circle cx="0" cy="0" r="14" fill="#10b981" stroke="#059669" stroke-width="2" filter="url(#pulley-shadow)" />
              <text x="0" y="5" font-size="12" text-anchor="middle">🖐️</text>
              <text x="24" y="5" fill="#047857" font-family="Prompt" font-weight="700" font-size="13">ดึง ${this.state.mass} kg</text>
            </g>
          `;
          layer.innerHTML = html;
        } else if (this.state.type === 'movable') {
          // Movable Pulley with ceiling guide pulley
          const pFixedX = 430, pFixedY = 65, r = 22;
          const pMovX = 350, rMov = 24;
          const pMovY = loadBoxY - rMov - 10;
          const anchorX = 300;
          const handY = 120 + currentLiftPx * 2;

          let html = `
            <!-- Ceiling Anchor -->
            <circle cx="${anchorX}" cy="${ceilingY}" r="5" fill="#334155" />
            <rect x="${pFixedX - 3}" y="${ceilingY}" width="6" height="${pFixedY - ceilingY}" fill="#64748b" />
            <!-- Fixed guide pulley -->
            <circle cx="${pFixedX}" cy="${pFixedY}" r="${r}" fill="url(#pulley-metal)" stroke="#334155" stroke-width="2" />
            <!-- Movable pulley and hanger -->
            <circle cx="${pMovX}" cy="${pMovY}" r="${rMov}" fill="url(#pulley-metal)" stroke="#334155" stroke-width="2.5" filter="url(#pulley-shadow)" />
            <circle cx="${pMovX}" cy="${pMovY}" r="4" fill="#ef4444" />
            <line x1="${pMovX}" y1="${pMovY + rMov}" x2="${pMovX}" y2="${loadBoxY}" stroke="#475569" stroke-width="3" />
            <!-- Load Box -->
            <rect x="${pMovX - boxW/2}" y="${loadBoxY}" width="${boxW}" height="${boxH}" rx="6" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2" filter="url(#pulley-shadow)" />
            <text x="${pMovX}" y="${loadBoxY + 30}" fill="#ffffff" font-family="Prompt" font-weight="700" font-size="14" text-anchor="middle">${this.state.mass} kg</text>
            <!-- Ropes -->
            <line x1="${anchorX}" y1="${ceilingY}" x2="${pMovX - rMov}" y2="${pMovY}" stroke="#d97706" stroke-width="3.5" />
            <path d="M ${pMovX - rMov} ${pMovY} A ${rMov} ${rMov} 0 0 0 ${pMovX + rMov} ${pMovY}" fill="none" stroke="#d97706" stroke-width="3.5" />
            <line x1="${pMovX + rMov}" y1="${pMovY}" x2="${pFixedX - r}" y2="${pFixedY}" stroke="#d97706" stroke-width="3.5" />
            <path d="M ${pFixedX - r} ${pFixedY} A ${r} ${r} 0 0 1 ${pFixedX + r} ${pFixedY}" fill="none" stroke="#d97706" stroke-width="3.5" />
            <line x1="${pFixedX + r}" y1="${pFixedY}" x2="${pFixedX + r}" y2="${handY}" stroke="#d97706" stroke-width="3.5" />
            <!-- Pull Handle -->
            <g id="pulley-pull-handle" style="cursor: ns-resize;" transform="translate(${pFixedX + r}, ${handY})">
              <circle cx="0" cy="0" r="14" fill="#10b981" stroke="#059669" stroke-width="2" filter="url(#pulley-shadow)" />
              <text x="0" y="5" font-size="12" text-anchor="middle">🖐️</text>
              <text x="24" y="5" fill="#047857" font-family="Prompt" font-weight="700" font-size="13">ดึง ${forceKg.toFixed(1)} kg</text>
            </g>
          `;
          layer.innerHTML = html;
        } else {
          // Compound Pulley (Block and tackle with n strands)
          const pxTop = 380, pyTop = 70;
          const pyBottom = loadBoxY - 35;
          const pullX = 460;
          const handY = 100 + Math.min(200, currentLiftPx * n * 0.7);

          let html = `
            <!-- Upper Block Mount -->
            <rect x="${pxTop - 25}" y="${ceilingY}" width="50" height="20" fill="#64748b" rx="3" />
            <!-- Upper Pulleys -->
            <circle cx="${pxTop - 12}" cy="${pyTop}" r="22" fill="url(#pulley-metal)" stroke="#334155" stroke-width="2" />
            <circle cx="${pxTop + 12}" cy="${pyTop}" r="22" fill="url(#pulley-metal)" stroke="#334155" stroke-width="2" />
            <!-- Lower Block & Pulleys -->
            <g transform="translate(${pxTop}, ${pyBottom})">
              <circle cx="-10" cy="0" r="20" fill="url(#pulley-metal)" stroke="#334155" stroke-width="2" filter="url(#pulley-shadow)" />
              <circle cx="10" cy="0" r="20" fill="url(#pulley-metal)" stroke="#334155" stroke-width="2" filter="url(#pulley-shadow)" />
              <line x1="0" y1="20" x2="0" y2="35" stroke="#334155" stroke-width="3" />
            </g>
            <!-- Load Box -->
            <rect x="${pxTop - boxW/2}" y="${loadBoxY}" width="${boxW}" height="${boxH}" rx="6" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2" filter="url(#pulley-shadow)" />
            <text x="${pxTop}" y="${loadBoxY + 30}" fill="#ffffff" font-family="Prompt" font-weight="700" font-size="14" text-anchor="middle">${this.state.mass} kg</text>
            <!-- Vertical Ropes between blocks (${n} strands) -->
          `;

          // Generate n rope strands
          const leftOffsets = [-24, -12, 0, 12, 24];
          for (let i = 0; i < n; i++) {
            const rx = pxTop + (i - (n - 1) / 2) * 12;
            html += `<line x1="${rx}" y1="${pyTop + 10}" x2="${rx}" y2="${pyBottom - 10}" stroke="#d97706" stroke-width="3" />`;
          }

          // Guide to pull handle
          html += `
            <line x1="${pxTop + 24}" y1="${pyTop}" x2="${pullX}" y2="${pyTop}" stroke="#d97706" stroke-width="3.5" />
            <line x1="${pullX}" y1="${pyTop}" x2="${pullX}" y2="${handY}" stroke="#d97706" stroke-width="3.5" />
            <g id="pulley-pull-handle" style="cursor: ns-resize;" transform="translate(${pullX}, ${handY})">
              <circle cx="0" cy="0" r="14" fill="#10b981" stroke="#059669" stroke-width="2" filter="url(#pulley-shadow)" />
              <text x="0" y="5" font-size="12" text-anchor="middle">🖐️</text>
              <text x="24" y="5" fill="#047857" font-family="Prompt" font-weight="700" font-size="13">ดึง ${forceKg.toFixed(1)} kg</text>
            </g>
          `;
          layer.innerHTML = html;
        }

        // Height indicator arrow on left
        const arrowX = 140;
        scaleLayer.innerHTML = `
          <line x1="${arrowX}" y1="${groundY}" x2="${arrowX}" y2="${loadBoxY + boxH}" stroke="#3b82f6" stroke-width="2" stroke-dasharray="3,3" />
          <circle cx="${arrowX}" cy="${groundY}" r="3" fill="#3b82f6" />
          <circle cx="${arrowX}" cy="${loadBoxY + boxH}" r="3" fill="#3b82f6" />
          <text x="${arrowX - 10}" y="${(groundY + loadBoxY + boxH) / 2 + 5}" fill="#1d4ed8" font-family="Prompt" font-size="12" font-weight="700" text-anchor="end">h = ${h.toFixed(2)} m</text>
        `;
      },
      setupDragging() {
        const svg = document.getElementById('pulley-svg');
        let isDragging = false;
        let startY = 0;
        let startHeight = 0;

        const onStart = (e) => {
          const target = e.target.closest('#pulley-pull-handle');
          if (!target) return;
          e.preventDefault();
          isDragging = true;
          startY = e.touches ? e.touches[0].clientY : e.clientY;
          startHeight = this.state.liftHeight;
          Sound.click();
        };

        const onMove = (e) => {
          if (!isDragging) return;
          e.preventDefault();
          const currentY = e.touches ? e.touches[0].clientY : e.clientY;
          const deltaY = currentY - startY;
          // Dragging handle down increases lift height
          const newH = Math.max(0.0, Math.min(1.6, startHeight + (deltaY / 100)));
          document.getElementById('slider-pulley-height').value = newH.toFixed(2);
          this.onControlChange();
        };

        const onEnd = () => { isDragging = false; };

        svg.addEventListener('mousedown', onStart);
        svg.addEventListener('touchstart', onStart, { passive: false });
        window.addEventListener('mousemove', onMove);
        window.addEventListener('touchmove', onMove, { passive: false });
        window.addEventListener('mouseup', onEnd);
        window.addEventListener('touchend', onEnd);
      },
      setPreset(name) {
        Sound.click();
        if (name === 'fixed') {
          this.setType('fixed');
          document.getElementById('slider-pulley-mass').value = 40;
          document.getElementById('slider-pulley-height').value = 0.5;
        } else if (name === 'movable') {
          this.setType('movable');
          document.getElementById('slider-pulley-mass').value = 40;
          document.getElementById('slider-pulley-height').value = 0.6;
        } else if (name === 'compound-4') {
          this.setType('compound');
          document.getElementById('slider-pulley-strands').value = 4;
          document.getElementById('val-pulley-strands').textContent = '4 เส้น';
          this.state.strands = 4;
          document.getElementById('slider-pulley-mass').value = 60;
          document.getElementById('slider-pulley-height').value = 0.6;
        }
        this.onControlChange();
      },
      simulatePullAnimation() {
        if (this.state.isSimulating) return;
        this.state.isSimulating = true;
        Sound.click();
        let step = 0;
        const initialH = 0.1;
        const targetH = 1.4;
        const interval = setInterval(() => {
          step++;
          if (step <= 30) {
            const cur = initialH + (targetH - initialH) * (step / 30);
            document.getElementById('slider-pulley-height').value = cur.toFixed(2);
            this.onControlChange();
          } else if (step <= 45) {
          } else if (step <= 75) {
            const cur = targetH - (targetH - 0.6) * ((step - 45) / 30);
            document.getElementById('slider-pulley-height').value = cur.toFixed(2);
            this.onControlChange();
          } else {
            clearInterval(interval);
            this.state.isSimulating = false;
          }
        }, 30);
      },
      loadPredictionScenario(idx) {
        this.predictionState.currentScenario = idx;
        const sc = this.predictionState.scenarios[idx];
        document.getElementById('pulley-predict-q-title').textContent = sc.title;
        document.getElementById('pulley-predict-q-desc').textContent = sc.desc;
        const container = document.getElementById('pulley-predict-options-container');
        container.innerHTML = '';
        sc.options.forEach((optText, i) => {
          const letter = ['ก', 'ข', 'ค'][i];
          const btn = document.createElement('button');
          btn.className = 'predict-option-btn';
          btn.onclick = () => this.selectPredictionOption(i);
          btn.innerHTML = `<span class="opt-badge">${letter}</span><span>${optText}</span>`;
          container.appendChild(btn);
        });
        document.getElementById('btn-run-pulley-predict').disabled = true;
        document.getElementById('pulley-predict-result-box').style.display = 'none';
      },
      selectPredictionOption(index) {
        Sound.click();
        this.predictionState.selectedOption = index;
        const btns = document.querySelectorAll('#pulley-predict-options-container .predict-option-btn');
        btns.forEach((b, i) => {
          if (i === index) b.classList.add('selected'); else b.classList.remove('selected');
        });
        document.getElementById('btn-run-pulley-predict').disabled = false;
      },
      executePredictionTest() {
        const sc = this.predictionState.scenarios[this.predictionState.currentScenario];
        const isCorrect = this.predictionState.selectedOption === sc.correct;
        this.setType(sc.setup.type);
        if (sc.setup.type === 'compound') {
          this.state.strands = sc.setup.strands;
          document.getElementById('slider-pulley-strands').value = sc.setup.strands;
        }
        document.getElementById('slider-pulley-mass').value = sc.setup.mass;
        document.getElementById('slider-pulley-height').value = 0.8;
        this.onControlChange();

        const fbBox = document.getElementById('pulley-predict-result-box');
        fbBox.style.display = 'block';
        if (isCorrect) {
          Sound.correctFanfare();
          fbBox.className = 'predict-result-box correct';
          document.getElementById('pulley-predict-fb-title').innerHTML = '🎉 ถูกต้องแม่นยำ!';
          document.getElementById('pulley-predict-fb-text').innerHTML = sc.explanation;
        } else {
          Sound.wrongTone();
          fbBox.className = 'predict-result-box incorrect';
          document.getElementById('pulley-predict-fb-title').innerHTML = '🧐 คำตอบจริงเป็นอีกแบบ ลองดูการจำลองสิ!';
          document.getElementById('pulley-predict-fb-text').innerHTML = `${sc.explanation} (สังเกตผลที่แผงวัดผลสด)`;
        }
      },
      nextPredictionScenario() {
        Sound.click();
        const next = (this.predictionState.currentScenario + 1) % this.predictionState.scenarios.length;
        this.loadPredictionScenario(next);
      },
      loadMission(num) {
        Sound.click();
        this.switchTab('explore');
        if (num === 1) {
          this.setType('fixed'); // User must change to movable
          document.getElementById('slider-pulley-mass').value = 30;
          document.getElementById('slider-pulley-height').value = 0.5;
        } else if (num === 2) {
          this.setType('fixed'); // User must change to compound >= 4
          document.getElementById('slider-pulley-mass').value = 60;
          document.getElementById('slider-pulley-height').value = 0.6;
        } else if (num === 3) {
          this.setType('compound');
          document.getElementById('slider-pulley-strands').value = 5;
          this.state.strands = 5;
          document.getElementById('slider-pulley-mass').value = 50;
          document.getElementById('slider-pulley-height').value = 0.3; // User should set to 1.2
        }
        this.onControlChange();
      },
      checkMission(num) {
        const { type, strands, mass, liftHeight } = this.state;
        const fb = document.getElementById(`pmission-fb-${num}`);
        fb.style.display = 'block';

        if (num === 1) {
          if (type === 'movable' && mass === 30) {
            fb.style.color = '#059669';
            fb.textContent = '🎉 ยอดเยี่ยมมาก! ใช้รอกเดี่ยวเคลื่อนที่ ยกของ 30 กก. ด้วยแรงเพียง 15 กก. ได้รับ 1 ดาว ⭐';
            App.awardStar('pulley', 'm1');
            this.updateMissionsUI();
          } else {
            Sound.wrongTone();
            fb.style.color = '#dc2626';
            fb.textContent = 'ยังไม่ผ่านนะ! ต้องเลือกรอกเดี่ยวเคลื่อนที่ เพื่อให้ทุ่นแรงครึ่งหนึ่งเหลือ 15 กก.';
          }
        } else if (num === 2) {
          const currentForce = (type === 'compound') ? (mass / strands) : (type === 'movable' ? mass / 2 : mass);
          if (mass === 60 && currentForce <= 15) {
            fb.style.color = '#059669';
            fb.textContent = `🎉 สำเร็จแล้ว! คุณใช้รอกที่มีเชือกรับน้ำหนัก ${strands} เส้น ออกแรงเพียง ${currentForce.toFixed(1)} กก. (ไม่เกิน 15 กก.) ได้รับ 1 ดาว ⭐`;
            App.awardStar('pulley', 'm2');
            this.updateMissionsUI();
          } else {
            Sound.wrongTone();
            fb.style.color = '#dc2626';
            fb.textContent = `แรงที่ใช้อยู่ที่ ${currentForce.toFixed(1)} กก. ยังเกิน 15 กก. อยู่! แนะนำให้ใช้รอกพวงที่มีเชือกอย่างน้อย 4 เส้นนะ`;
          }
        } else if (num === 3) {
          if (type === 'compound' && strands === 5 && mass === 50 && Math.abs(liftHeight - 1.2) < 0.1) {
            const work = 500 * 1.2;
            fb.style.color = '#059669';
            fb.textContent = `🎉 สุดยอด! ยกสูง 1.2 ม. ต้องดึงเชือก ${ (1.2 * 5).toFixed(1) } ม. งานที่ทำ = ${work} จูล เท่ากันเป๊ะ! ได้รับ 1 ดาว ⭐`;
            App.awardStar('pulley', 'm3');
            this.updateMissionsUI();
          } else {
            Sound.wrongTone();
            fb.style.color = '#dc2626';
            fb.textContent = 'ยังไม่ครบเงื่อนไขนะ! ต้องใช้รอกพวง 5 เส้น มวล 50 กก. และปรับความสูงให้เป็น 1.2 เมตร';
          }
        }
      },
      updateMissionsUI() {
        const stars = App.state.stars.pulley || {};
        ['m1', 'm2', 'm3'].forEach((mKey, idx) => {
          const num = idx + 1;
          const card = document.getElementById(`pmission-card-${num}`);
          const starIcon = document.getElementById(`pmstar-${num}`);
          if (stars[mKey]) {
            card.classList.add('completed');
            starIcon.textContent = '⭐ ได้รับแล้ว!';
          } else {
            card.classList.remove('completed');
            starIcon.textContent = '⭐';
          }
        });
      },
      submitQuiz() {
        Sound.click();
        const form = document.getElementById('pulley-quiz-form');
        const answers = { pq1: 'b', pq2: 'a', pq3: 'b', pq4: 'c' };
        let score = 0;
        ['pq1', 'pq2', 'pq3', 'pq4'].forEach(q => {
          const selected = form.elements[q].value;
          document.getElementById(`exp-${q}`).style.display = 'block';
          form.querySelectorAll(`input[name="${q}"]`).forEach(r => {
            const lbl = r.parentElement;
            lbl.classList.remove('correct-answer', 'wrong-answer');
            if (r.value === answers[q]) lbl.classList.add('correct-answer');
            else if (r.checked && r.value !== answers[q]) lbl.classList.add('wrong-answer');
          });
          if (selected === answers[q]) score++;
        });
        const summary = document.getElementById('pulley-quiz-summary');
        summary.innerHTML = `ได้คะแนน: ${score} / 4 คะแนน`;
        if (score === 4) {
          Sound.correctFanfare();
          summary.innerHTML += ` 🎉 รับดาวควิซไปเลย ⭐`;
          App.awardStar('pulley', 'quiz');
        } else {
          Sound.wrongTone();
        }
      }
    };

    /* ==========================================================================
       ROOM 3: INCLINE LAB ENGINE (ห้องปฏิบัติการทางลาด)
       ========================================================================== */
    const InclineLab = {
      state: {
        height: 1.2,    // meters (0.5 to 2.4m)
        length: 3.6,    // meters (1.5 to 6.0m)
        mass: 60,       // kg
        friction: 0.0,  // 0.0, 0.05, 0.20
        cartProgress: 0.35, // 0.0 (bottom) to 1.0 (top)
        isSimulating: false
      },
      predictionState: {
        currentScenario: 0,
        selectedOption: null,
        scenarios: [
          {
            title: "สถานการณ์ที่ 1: ถ้าเพิ่มความยาวทางลาด (L) ให้ยาวขึ้น แต่ความสูงเท่าเดิม...",
            desc: "หากต้องการเข็นกล่องขึ้นท้ายรถบรรทุกสูง 1 เมตร ถ้ายืดทางลาดให้ยาวขึ้นจาก 2 เมตรเป็น 4 เมตร (ชันน้อยลง) แรงที่ต้องใช้ดันจะ...",
            options: [
              "ลดลงครึ่งหนึ่ง (ออกแรงเบาลงมาก)",
              "เพิ่มขึ้นเป็น 2 เท่า (หนักแรงกว่าเดิม)",
              "เท่าเดิม เพราะความสูงยังคงเป็น 1 เมตรเท่าเดิม"
            ],
            correct: 0,
            setup: { height: 1.0, length: 4.0, mass: 40, friction: 0 },
            explanation: "ถูกต้องเลย! จากสูตร F = W × (h ÷ L) เมื่อทางลาด L ยาวขึ้น ความชันจะน้อยลง ทำให้แรงต้านที่ต้องเอาชนะลดลง ออกแรงเบาลงครึ่งหนึ่งทันที!"
          },
          {
            title: "สถานการณ์ที่ 2: ขนถังน้ำมัน 60 กก. ขึ้นสูง 1 เมตร ด้วยทางลาดยาว 3 เมตร...",
            desc: "ถังน้ำมันหนัก 60 กก. (600 N) หากเข็นขึ้นทางลาดยาว 3 เมตร สูง 1 เมตร (ไม่มีความฝืด) จะต้องออกแรงดันกี่กิโลกรัม?",
            options: [
              "ออกแรงประมาณ 20 กิโลกรัม (200 N)",
              "ออกแรง 30 กิโลกรัม",
              "ออกแรง 60 กิโลกรัม เท่าเดิม"
            ],
            correct: 0,
            setup: { height: 1.0, length: 3.0, mass: 60, friction: 0 },
            explanation: "ยอดเยี่ยมมาก! แรงดัน F = W × (h ÷ L) = 60 × (1 ÷ 3) = 20 กก. (200 N) ทุ่นแรงได้ถึง 3 เท่า!"
          },
          {
            title: "สถานการณ์ที่ 3: กฎของงานบนทางลาด (เมื่อไม่มีแรงเสียดทาน)...",
            desc: "งานที่ใช้เข็นกล่องขึ้นตามทางลาด (แรงดัน × ทางลาดยาว) เทียบกับงานที่ยกกล่องขึ้นตรงๆ ในแนวดิ่ง (น้ำหนัก × ความสูง) จะเป็นอย่างไร?",
            options: [
              "บนทางลาดทำงานน้อยกว่าการยกตรงๆ",
              "ได้งานเท่ากันเป๊ะ ตามกฎการอนุรักษ์พลังงาน",
              "ยกตรงๆ ทำงานน้อยกว่าเพราะระยะทางสั้นกว่า"
            ],
            correct: 1,
            setup: { height: 1.2, length: 3.6, mass: 50, friction: 0 },
            explanation: "เป๊ะเลย! เครื่องกลไม่ได้ช่วยลดงาน (งาน = แรง × ระยะทาง) บนทางลาดเราออกแรงน้อยลง แต่ต้องเข็นด้วยระยะทางที่ไกลขึ้น งานทั้งสองแบบจึงเท่ากันเป๊ะเสมอ!"
          }
        ]
      },
      init() {
        this.setupDragging();
        this.onControlChange();
        this.loadPredictionScenario(0);
        this.updateMissionsUI();
      },
      switchTab(tabId) {
        Sound.click();
        const tabBtns = document.querySelectorAll('#view-incline .tab-btn');
        const tabPanels = document.querySelectorAll('#view-incline .tab-content-panel');
        tabBtns.forEach(btn => btn.classList.remove('active'));
        tabPanels.forEach(p => p.classList.remove('active'));
        const targetTab = document.getElementById(`incline-tab-${tabId}`);
        if (targetTab) targetTab.classList.add('active');
        const map = { explore: 0, realworld: 1, predict: 2, missions: 3, quiz: 4 };
        if (tabBtns[map[tabId]]) tabBtns[map[tabId]].classList.add('active');
      },
      setFriction(mu) {
        Sound.click();
        this.state.friction = mu;
        document.querySelectorAll('#view-incline .pill-selector button').forEach(b => b.classList.remove('active'));
        if (mu === 0.0) document.getElementById('btn-fric-none').classList.add('active');
        else if (mu === 0.05) document.getElementById('btn-fric-wheels').classList.add('active');
        else if (mu === 0.20) document.getElementById('btn-fric-rough').classList.add('active');
        this.onControlChange();
      },
      stepMass(delta) {
        Sound.click();
        const el = document.getElementById('slider-incline-mass');
        el.value = Math.max(10, Math.min(100, parseInt(el.value) + delta));
        this.onControlChange();
      },
      onControlChange() {
        this.state.height = parseFloat(document.getElementById('slider-incline-height').value);
        let len = parseFloat(document.getElementById('slider-incline-length').value);
        // Ramp length must be strictly greater than height
        if (len <= this.state.height + 0.2) {
          len = this.state.height + 0.2;
          document.getElementById('slider-incline-length').value = len.toFixed(1);
        }
        this.state.length = len;
        this.state.mass = parseFloat(document.getElementById('slider-incline-mass').value);
        this.updatePhysicsAndUI();
      },
      updatePhysicsAndUI() {
        const { height, length, mass, friction } = this.state;
        const weightN = mass * 10;
        const sinTheta = height / length;
        const angleDeg = (Math.asin(sinTheta) * 180 / Math.PI).toFixed(1);

        // Friction force: f = mu * N = mu * W * cos(theta)
        const cosTheta = Math.sqrt(Math.max(0, 1 - sinTheta * sinTheta));
        const idealForceN = weightN * sinTheta;
        const frictionForceN = friction * weightN * cosTheta;
        const totalForceN = idealForceN + frictionForceN;
        const totalForceKg = totalForceN / 10;
        const ma = (length / height).toFixed(2);

        const workRampJoules = totalForceN * length;
        const workLiftJoules = weightN * height;

        // UI Labels
        document.getElementById('val-incline-height').textContent = `${height.toFixed(1)} ม.`;
        document.getElementById('val-incline-length').textContent = `${length.toFixed(1)} ม.`;
        document.getElementById('tag-incline-angle').textContent = `${angleDeg}°`;
        document.getElementById('tag-incline-ratio').textContent = `1 : ${(length/height).toFixed(1)}`;
        document.getElementById('tag-incline-mass').textContent = `${mass} kg (${weightN} N)`;

        document.getElementById('metric-incline-w').textContent = `${weightN} N (${mass} kg)`;
        document.getElementById('metric-incline-f').textContent = `${totalForceN.toFixed(0)} N (${totalForceKg.toFixed(1)} kg)`;
        document.getElementById('metric-incline-f-desc').textContent = friction > 0 ? `รวมแรงเสียดทาน +${frictionForceN.toFixed(0)} N` : `ทุ่นแรงได้ ${ma} เท่า!`;

        document.getElementById('metric-incline-ma').textContent = `${ma} เท่า`;
        document.getElementById('metric-incline-work').textContent = `${workRampJoules.toFixed(0)} จูล`;
        document.getElementById('metric-incline-work-desc').textContent = friction > 0 ? `(งานยกตรงๆ = ${workLiftJoules.toFixed(0)} J + ความร้อน)` : `(เท่ากับงานยกตรงๆ ${workLiftJoules.toFixed(0)} J)`;

        document.getElementById('work-incline-explanation').innerHTML = `
          ถ้ายกกล่อง <strong>${weightN} N</strong> ขึ้นตรงๆ สูง <strong>${height.toFixed(1)} ม.</strong> งานที่ได้ = <strong>${workLiftJoules.toFixed(0)} จูล (J)</strong><br>
          เมื่อใช้ทางลาดยาว <strong>${length.toFixed(1)} ม.</strong> ออกแรงเพียง <strong>${totalForceN.toFixed(0)} N</strong> แต่ต้องเข็นเป็นระยะทาง <strong>${length.toFixed(1)} ม.</strong> 
          งานที่ทำ = ${totalForceN.toFixed(0)} N × ${length.toFixed(1)} ม. = <strong>${workRampJoules.toFixed(0)} จูล (J)</strong>
          ${friction === 0 ? ' (งานเท่ากันเป๊ะตามกฎการอนุรักษ์พลังงาน!)' : ' (งานเพิ่มขึ้นเล็กน้อยเนื่องจากแรงเสียดทานเปลี่ยนเป็นความร้อน)'}
        `;

        this.renderSvg(height, length, angleDeg, totalForceN, weightN);
      },
      renderSvg(h, L, angleDeg, forceN, weightN) {
        const groundY = 330;
        const xStart = 80;
        const xPlatform = 620;
        // Compute SVG height proportional to physical height
        const maxH = 2.4;
        const maxRampPx = 170;
        const rampHPx = (h / maxH) * maxRampPx;
        const yTop = groundY - rampHPx;

        // Base width on SVG
        const basePx = xPlatform - xStart;

        // Update Ramp Polygon
        const rampPoly = document.getElementById('ramp-triangle');
        rampPoly.setAttribute('points', `${xStart},${groundY} ${xPlatform},${groundY} ${xPlatform},${yTop}`);

        // Update Top Platform
        const plat = document.getElementById('top-platform');
        plat.setAttribute('x', xPlatform);
        plat.setAttribute('y', yTop);
        plat.setAttribute('height', groundY - yTop);
        document.getElementById('top-platform-label').setAttribute('y', (yTop + groundY) / 2 + 5);

        // Dimensions layer
        const dimLayer = document.getElementById('incline-dimensions-layer');
        dimLayer.innerHTML = `
          <!-- Height dimension arrow -->
          <line x1="${xPlatform + 110}" y1="${groundY}" x2="${xPlatform + 110}" y2="${yTop}" stroke="#6d28d9" stroke-width="2" />
          <circle cx="${xPlatform + 110}" cy="${groundY}" r="3" fill="#6d28d9" />
          <circle cx="${xPlatform + 110}" cy="${yTop}" r="3" fill="#6d28d9" />
          <text x="${xPlatform + 118}" y="${(groundY + yTop)/2 + 5}" fill="#6d28d9" font-family="Prompt" font-weight="700" font-size="13">h = ${h.toFixed(1)} m</text>
          
          <!-- Angle arc at corner -->
          <path d="M ${xStart + 40} ${groundY} A 40 40 0 0 0 ${xStart + 36} ${groundY - 14}" fill="none" stroke="#2563eb" stroke-width="2" />
          <text x="${xStart + 50}" y="${groundY - 8}" fill="#1d4ed8" font-family="Prompt" font-weight="700" font-size="12">θ = ${angleDeg}°</text>
        `;

        // Cart Position on Hypotenuse
        const p = this.state.cartProgress;
        const cartX = xStart + p * (xPlatform - xStart);
        const cartY = groundY - p * (groundY - yTop);
        const angleRad = -Math.atan2(groundY - yTop, xPlatform - xStart);
        const rotDeg = angleRad * 180 / Math.PI;

        const cartGroup = document.getElementById('incline-cart-group');
        cartGroup.setAttribute('transform', `translate(${cartX}, ${cartY}) rotate(${rotDeg})`);

        cartGroup.innerHTML = `
          <!-- Cart Body -->
          <rect x="-35" y="-36" width="70" height="36" rx="6" fill="#10b981" stroke="#047857" stroke-width="2.5" filter="url(#incline-shadow)" />
          <text x="0" y="-14" fill="#ffffff" font-family="Prompt" font-weight="700" font-size="13" text-anchor="middle">${this.state.mass} kg</text>
          <!-- Wheels -->
          <circle cx="-20" cy="0" r="7" fill="#334155" stroke="#ffffff" stroke-width="1.5" />
          <circle cx="20" cy="0" r="7" fill="#334155" stroke="#ffffff" stroke-width="1.5" />
          <!-- Push Force Vector Arrow -->
          <line x1="-35" y1="-18" x2="60" y2="-18" stroke="#f59e0b" stroke-width="3.5" marker-end="url(#arrow)" />
          <polygon points="60,-22 72,-18 60,-14" fill="#f59e0b" />
          <text x="40" y="-26" fill="#b45309" font-family="Prompt" font-weight="700" font-size="12">F = ${forceN.toFixed(0)} N</text>
        `;
      },
      setupDragging() {
        const svg = document.getElementById('incline-svg');
        let isDragging = false;
        const xStart = 80;
        const xPlatform = 620;

        const getCoords = (e) => {
          const pt = svg.createSVGPoint();
          if (e.touches && e.touches.length > 0) {
            pt.x = e.touches[0].clientX; pt.y = e.touches[0].clientY;
          } else {
            pt.x = e.clientX; pt.y = e.clientY;
          }
          return pt.matrixTransform(svg.getScreenCTM().inverse());
        };

        const onStart = (e) => {
          const target = e.target.closest('#incline-cart-group');
          if (!target) return;
          e.preventDefault();
          isDragging = true;
          Sound.click();
        };

        const onMove = (e) => {
          if (!isDragging) return;
          e.preventDefault();
          const coords = getCoords(e);
          const p = Math.max(0.05, Math.min(0.95, (coords.x - xStart) / (xPlatform - xStart)));
          this.state.cartProgress = p;
          this.updatePhysicsAndUI();
        };

        const onEnd = () => { isDragging = false; };

        svg.addEventListener('mousedown', onStart);
        svg.addEventListener('touchstart', onStart, { passive: false });
        window.addEventListener('mousemove', onMove);
        window.addEventListener('touchmove', onMove, { passive: false });
        window.addEventListener('mouseup', onEnd);
        window.addEventListener('touchend', onEnd);
      },
      setPreset(name) {
        Sound.click();
        if (name === 'gentle') {
          document.getElementById('slider-incline-height').value = 1.0;
          document.getElementById('slider-incline-length').value = 5.0;
          document.getElementById('slider-incline-mass').value = 50;
          this.setFriction(0.0);
        } else if (name === 'steep') {
          document.getElementById('slider-incline-height').value = 2.0;
          document.getElementById('slider-incline-length').value = 2.5;
          document.getElementById('slider-incline-mass').value = 50;
          this.setFriction(0.0);
        } else if (name === 'disabled-ramp') {
          document.getElementById('slider-incline-height').value = 0.5;
          document.getElementById('slider-incline-length').value = 6.0;
          document.getElementById('slider-incline-mass').value = 70;
          this.setFriction(0.05);
        }
        this.onControlChange();
      },
      simulatePushAnimation() {
        if (this.state.isSimulating) return;
        this.state.isSimulating = true;
        Sound.click();
        let step = 0;
        const initialP = 0.05;
        const targetP = 0.95;
        const interval = setInterval(() => {
          step++;
          if (step <= 35) {
            this.state.cartProgress = initialP + (targetP - initialP) * (step / 35);
            this.updatePhysicsAndUI();
          } else if (step <= 50) {
          } else if (step <= 80) {
            this.state.cartProgress = targetP - (targetP - 0.35) * ((step - 50) / 30);
            this.updatePhysicsAndUI();
          } else {
            clearInterval(interval);
            this.state.isSimulating = false;
          }
        }, 30);
      },
      loadPredictionScenario(idx) {
        this.predictionState.currentScenario = idx;
        const sc = this.predictionState.scenarios[idx];
        document.getElementById('incline-predict-q-title').textContent = sc.title;
        document.getElementById('incline-predict-q-desc').textContent = sc.desc;
        const container = document.getElementById('incline-predict-options-container');
        container.innerHTML = '';
        sc.options.forEach((optText, i) => {
          const letter = ['ก', 'ข', 'ค'][i];
          const btn = document.createElement('button');
          btn.className = 'predict-option-btn';
          btn.onclick = () => this.selectPredictionOption(i);
          btn.innerHTML = `<span class="opt-badge">${letter}</span><span>${optText}</span>`;
          container.appendChild(btn);
        });
        document.getElementById('btn-run-incline-predict').disabled = true;
        document.getElementById('incline-predict-result-box').style.display = 'none';
      },
      selectPredictionOption(index) {
        Sound.click();
        this.predictionState.selectedOption = index;
        const btns = document.querySelectorAll('#incline-predict-options-container .predict-option-btn');
        btns.forEach((b, i) => {
          if (i === index) b.classList.add('selected'); else b.classList.remove('selected');
        });
        document.getElementById('btn-run-incline-predict').disabled = false;
      },
      executePredictionTest() {
        const sc = this.predictionState.scenarios[this.predictionState.currentScenario];
        const isCorrect = this.predictionState.selectedOption === sc.correct;
        document.getElementById('slider-incline-height').value = sc.setup.height;
        document.getElementById('slider-incline-length').value = sc.setup.length;
        document.getElementById('slider-incline-mass').value = sc.setup.mass;
        this.setFriction(sc.setup.friction);
        this.onControlChange();

        const fbBox = document.getElementById('incline-predict-result-box');
        fbBox.style.display = 'block';
        if (isCorrect) {
          Sound.correctFanfare();
          fbBox.className = 'predict-result-box correct';
          document.getElementById('incline-predict-fb-title').innerHTML = '🎉 ถูกต้องแม่นยำ!';
          document.getElementById('incline-predict-fb-text').innerHTML = sc.explanation;
        } else {
          Sound.wrongTone();
          fbBox.className = 'predict-result-box incorrect';
          document.getElementById('incline-predict-fb-title').innerHTML = '🧐 ผลจริงเป็นอีกแบบหนึ่ง ลองสังเกตดูสิ!';
          document.getElementById('incline-predict-fb-text').innerHTML = `${sc.explanation} (สังเกตผลที่แผงวัดผลสด)`;
        }
      },
      nextPredictionScenario() {
        Sound.click();
        const next = (this.predictionState.currentScenario + 1) % this.predictionState.scenarios.length;
        this.loadPredictionScenario(next);
      },
      loadMission(num) {
        Sound.click();
        this.switchTab('explore');
        if (num === 1) {
          document.getElementById('slider-incline-height').value = 1.0;
          document.getElementById('slider-incline-length').value = 1.5; // too short, requires > 10kg
          document.getElementById('slider-incline-mass').value = 30;
          this.setFriction(0.0);
        } else if (num === 2) {
          document.getElementById('slider-incline-height').value = 1.2;
          document.getElementById('slider-incline-length').value = 2.0; // requires adjustment to >= 4.8
          document.getElementById('slider-incline-mass').value = 60;
          this.setFriction(0.0);
        } else if (num === 3) {
          document.getElementById('slider-incline-height').value = 1.0;
          document.getElementById('slider-incline-length').value = 2.0;
          document.getElementById('slider-incline-mass').value = 50;
          this.setFriction(0.20); // rough surface
        }
        this.onControlChange();
      },
      checkMission(num) {
        const { height, length, mass, friction } = this.state;
        const weightN = mass * 10;
        const sinTheta = height / length;
        const cosTheta = Math.sqrt(Math.max(0, 1 - sinTheta * sinTheta));
        const totalForceKg = (weightN * sinTheta + friction * weightN * cosTheta) / 10;

        const fb = document.getElementById(`imission-fb-${num}`);
        fb.style.display = 'block';

        if (num === 1) {
          if (mass === 30 && Math.abs(height - 1.0) < 0.1 && totalForceKg <= 10.1) {
            fb.style.color = '#059669';
            fb.textContent = `🎉 ผ่านแล้ว! คุณใช้ทางลาดยาว ${length.toFixed(1)} ม. ออกแรงเพียง ${totalForceKg.toFixed(1)} กก. (ไม่เกิน 10 กก.) ได้รับ 1 ดาว ⭐`;
            App.awardStar('incline', 'm1');
            this.updateMissionsUI();
          } else {
            Sound.wrongTone();
            fb.style.color = '#dc2626';
            fb.textContent = `แรงดันตอนนี้คือ ${totalForceKg.toFixed(1)} กก. (เกิน 10 กก.) ลองเพิ่มความยาวทางลาดให้ยาวขึ้นอย่างน้อย 3.0 เมตรดูสิ`;
          }
        } else if (num === 2) {
          if (mass === 60 && Math.abs(height - 1.2) < 0.1 && totalForceKg <= 15.1) {
            fb.style.color = '#059669';
            fb.textContent = `🎉 สำเร็จแล้ว! ปรับทางลาดยาว ${length.toFixed(1)} ม. ออกแรงดันเพียง ${totalForceKg.toFixed(1)} กก. ขนขึ้นรถได้สบาย ได้รับ 1 ดาว ⭐`;
            App.awardStar('incline', 'm2');
            this.updateMissionsUI();
          } else {
            Sound.wrongTone();
            fb.style.color = '#dc2626';
            fb.textContent = `แรงดันตอนนี้อยู่ที่ ${totalForceKg.toFixed(1)} กก. (ยังเกิน 15 กก.) แนะนำให้ปรับทางลาดยาวอย่างน้อย 4.8 เมตรนะ`;
          }
        } else if (num === 3) {
          if (mass === 50 && Math.abs(height - 1.0) < 0.1 && friction === 0.20 && totalForceKg <= 25.1) {
            fb.style.color = '#059669';
            fb.textContent = `🎉 สุดยอดนักวิทย์! เอาชนะแรงเสียดทานได้ ออกแรงเพียง ${totalForceKg.toFixed(1)} กก. ได้รับ 1 ดาว ⭐`;
            App.awardStar('incline', 'm3');
            this.updateMissionsUI();
          } else {
            Sound.wrongTone();
            fb.style.color = '#dc2626';
            fb.textContent = `ยังไม่ผ่านนะ! เปิดโหมดพื้นไม้หยาบ แรงดันตอนนี้คือ ${totalForceKg.toFixed(1)} กก. (เป้าหมายคือไม่เกิน 25 กก.) ลองเพิ่มความยาวทางลาดดูสิ`;
          }
        }
      },
      updateMissionsUI() {
        const stars = App.state.stars.incline || {};
        ['m1', 'm2', 'm3'].forEach((mKey, idx) => {
          const num = idx + 1;
          const card = document.getElementById(`imission-card-${num}`);
          const starIcon = document.getElementById(`imstar-${num}`);
          if (stars[mKey]) {
            card.classList.add('completed');
            starIcon.textContent = '⭐ ได้รับแล้ว!';
          } else {
            card.classList.remove('completed');
            starIcon.textContent = '⭐';
          }
        });
      },
      submitQuiz() {
        Sound.click();
        const form = document.getElementById('incline-quiz-form');
        const answers = { iq1: 'a', iq2: 'b', iq3: 'a', iq4: 'b' };
        let score = 0;
        ['iq1', 'iq2', 'iq3', 'iq4'].forEach(q => {
          const selected = form.elements[q].value;
          document.getElementById(`exp-${q}`).style.display = 'block';
          form.querySelectorAll(`input[name="${q}"]`).forEach(r => {
            const lbl = r.parentElement;
            lbl.classList.remove('correct-answer', 'wrong-answer');
            if (r.value === answers[q]) lbl.classList.add('correct-answer');
            else if (r.checked && r.value !== answers[q]) lbl.classList.add('wrong-answer');
          });
          if (selected === answers[q]) score++;
        });
        const summary = document.getElementById('incline-quiz-summary');
        summary.innerHTML = `ได้คะแนน: ${score} / 4 คะแนน`;
        if (score === 4) {
          Sound.correctFanfare();
          summary.innerHTML += ` 🎉 รับดาวควิซไปเลย ⭐`;
          App.awardStar('incline', 'quiz');
        } else {
          Sound.wrongTone();
        }
      }
    };

    window.addEventListener('DOMContentLoaded', () => {
      App.init();
    });
  </script>
</body>
</html>
''')

if __name__ == "__main__":
    generate()
