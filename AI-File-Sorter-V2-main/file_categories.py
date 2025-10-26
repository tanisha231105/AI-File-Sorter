"""
Comprehensive dataset for AI-based file organization.
Contains file patterns, keywords, and training examples for various categories.
"""

# File extensions for each category
FILE_PATTERNS = {
    # Documents and Text
    'documents': ['doc', 'docx', 'pdf', 'txt', 'rtf', 'odt', 'pages', 'md', 'tex', 'epub', 'gdoc', 'notion', 'wiki'],
    'spreadsheets': ['xls', 'xlsx', 'csv', 'ods', 'numbers', 'tsv', 'gsheet', 'airtable'],
    'presentations': ['ppt', 'pptx', 'key', 'odp', 'gslides', 'pitch'],
    
    # Media
    'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'webp', 'heic', 'raw', 'cr2', 'nef', 'psd', 'ai', 'sketch', 'tiff', 'ico', 'avif'],
    'videos': ['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv', 'webm', 'm4v', '3gp', 'mpeg', 'mpg', 'h264', 'prores', 'hevc'],
    'audio': ['mp3', 'wav', 'aac', 'flac', 'ogg', 'm4a', 'wma', 'aiff', 'opus', 'mid', 'midi', 'pcm', 'alac'],
    
    # Development
    'code': ['py', 'js', 'html', 'css', 'java', 'cpp', 'c', 'h', 'cs', 'php', 'rb', 'swift', 'kt', 'go', 'rs', 'ts', 'jsx', 'vue', 'svelte', 'dart', 'scala', 'r'],
    'data': ['json', 'xml', 'yaml', 'yml', 'sql', 'db', 'csv', 'parquet', 'avro', 'proto', 'hdf5', 'arrow', 'feather'],
    'config': ['ini', 'conf', 'cfg', 'env', 'properties', 'toml', 'lock', 'gradle', 'pom', 'dockerfile', 'terraform', 'helmfile'],
    
    # Archives and Executables
    'archives': ['zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz', 'iso', 'img', 'dmg'],
    'executables': ['exe', 'msi', 'bat', 'sh', 'app', 'dmg', 'deb', 'rpm', 'apk', 'ipa', 'appx', 'snap'],
    
    # Design and Creative
    'design': ['psd', 'ai', 'xd', 'sketch', 'fig', 'indd', 'ae', 'blend', 'c4d', 'afdesign', 'afphoto'],
    'fonts': ['ttf', 'otf', 'woff', 'woff2', 'eot', 'pfm', 'pfb', 'sfd'],
    '3d_models': ['obj', 'fbx', 'stl', '3ds', 'blend', 'dae', 'max', 'maya', 'c4d', 'usd', 'glb', 'gltf'],
    
    # Web and Cloud
    'web': ['html', 'css', 'js', 'php', 'jsx', 'vue', 'svelte', 'ts', 'tsx', 'wasm', 'webp', 'sass', 'less'],
    'cloud': ['gdoc', 'gsheet', 'gslide', 'gform', 'airtable', 'cform', 'notion'],
    
    # Project and Task Management
    'project': ['mpp', 'gan', 'prj', 'trello', 'jira', 'asana', 'monday', 'notion'],
    
    # Security and Certificates
    'security': ['key', 'pem', 'crt', 'cer', 'p12', 'pfx', 'keystore', 'jks', 'csr'],
    
    # Mobile Development
    'mobile': ['apk', 'ipa', 'aab', 'xcodeproj', 'pbxproj', 'gradle', 'plist', 'swift', 'kotlin'],
    
    # Machine Learning
    'ml_models': ['h5', 'pkl', 'pt', 'pth', 'onnx', 'tflite', 'pb', 'savedmodel', 'mlmodel', 'joblib'],
    
    # Container and Cloud Native
    'container': ['dockerfile', 'compose.yaml', 'k8s', 'helm', 'tf', 'tfstate'],
    
    # Game Development
    'game': ['unity', 'unreal', 'godot', 'blend', 'fbx', 'prefab', 'asset'],
    
    # CAD and Engineering
    'cad': ['dwg', 'dxf', 'step', 'stp', 'iges', 'ipt', 'iam', 'catpart']
}

# Keywords for content-based categorization
CONTENT_KEYWORDS = {
    'documents': [
        'report', 'document', 'note', 'paper', 'article', 'letter', 'memo', 'proposal',
        'contract', 'agreement', 'resume', 'cv', 'thesis', 'dissertation', 'essay',
        'review', 'summary', 'draft', 'manuscript', 'journal', 'publication', 'whitepaper',
        'specification', 'documentation', 'manual', 'guide', 'handbook', 'policy'
    ],
    'spreadsheets': [
        'budget', 'finance', 'expense', 'income', 'sales', 'inventory', 'data',
        'analysis', 'report', 'summary', 'forecast', 'metrics', 'tracking',
        'dashboard', 'calculation', 'worksheet', 'ledger', 'balance', 'statement',
        'analytics', 'pivot', 'chart', 'kpi', 'performance', 'statistics'
    ],
    'presentations': [
        'presentation', 'slide', 'deck', 'pitch', 'proposal', 'overview', 'summary',
        'review', 'meeting', 'conference', 'workshop', 'seminar', 'lecture',
        'showcase', 'demo', 'portfolio', 'roadmap', 'strategy', 'keynote',
        'webinar', 'training', 'course', 'lesson', 'orientation'
    ],
    'images': [
        'photo', 'image', 'picture', 'screenshot', 'snapshot', 'capture', 'shot',
        'graphic', 'design', 'art', 'wallpaper', 'banner', 'logo', 'icon',
        'thumbnail', 'avatar', 'profile', 'cover', 'scan', 'meme', 'infographic',
        'diagram', 'chart', 'illustration', 'mockup', 'wireframe'
    ],
    'videos': [
        'video', 'recording', 'clip', 'movie', 'film', 'tutorial', 'demo',
        'presentation', 'lecture', 'webinar', 'stream', 'vlog', 'episode',
        'series', 'animation', 'footage', 'reel', 'trailer', 'screencast',
        'timelapse', 'story', 'shorts', 'commercial', 'promo'
    ],
    'code': [
        'script', 'program', 'code', 'source', 'module', 'library', 'function',
        'class', 'method', 'algorithm', 'app', 'application', 'service', 'api',
        'backend', 'frontend', 'component', 'test', 'utils', 'helper', 'plugin',
        'extension', 'middleware', 'controller', 'model', 'view', 'hook', 'store'
    ],
    'project': [
        'project', 'task', 'milestone', 'timeline', 'roadmap', 'plan', 'schedule',
        'sprint', 'backlog', 'kanban', 'board', 'workflow', 'process', 'template',
        'checklist', 'todo', 'progress', 'status', 'report', 'epic', 'story',
        'feature', 'bug', 'issue', 'ticket', 'release', 'version'
    ],
    'design': [
        'design', 'mockup', 'wireframe', 'prototype', 'layout', 'template',
        'style', 'theme', 'brand', 'logo', 'icon', 'ui', 'ux', 'interface',
        'animation', 'illustration', 'graphic', 'artwork', 'asset', 'component',
        'pattern', 'color', 'typography', 'motion', 'interaction', 'styleguide'
    ],
    'ml_models': [
        'model', 'weights', 'training', 'dataset', 'neural', 'network', 'ai',
        'machine', 'learning', 'prediction', 'classification', 'regression',
        'clustering', 'detection', 'recognition', 'generation', 'transformer',
        'embedding', 'feature', 'checkpoint', 'hyperparameter', 'optimization'
    ],
    'container': [
        'container', 'docker', 'kubernetes', 'k8s', 'pod', 'deployment', 'service',
        'ingress', 'volume', 'config', 'secret', 'namespace', 'cluster', 'node',
        'registry', 'image', 'compose', 'stack', 'swarm', 'helm', 'chart'
    ],
    'game': [
        'game', 'level', 'map', 'asset', 'texture', 'model', 'animation', 'script',
        'shader', 'particle', 'sound', 'prefab', 'scene', 'character', 'enemy',
        'player', 'ui', 'menu', 'save', 'checkpoint', 'highscore', 'achievement'
    ]
}

# Common file name patterns
COMMON_PATTERNS = {
    'dates': [
        r'\d{4}-\d{2}-\d{2}',  # 2024-01-30
        r'\d{2}-\d{2}-\d{4}',  # 30-01-2024
        r'\d{8}',              # 20240130
        r'\d{2}_\d{2}_\d{4}',  # 30_01_2024
        r'\d{4}\d{2}\d{2}',    # 20240130
    ],
    'versions': [
        r'v\d+',              # v1, v2
        r'v\d+\.\d+',         # v1.0, v2.1
        r'v\d+\.\d+\.\d+',    # v1.0.0
        r'version\d+',        # version1
        r'rev\d+',           # rev1
        r'\d+\.\d+\.\d+',    # 1.0.0
    ],
    'status': [
        r'draft',
        r'final',
        r'review',
        r'approved',
        r'wip',
        r'done',
        r'pending',
        r'archived',
        r'deprecated',
        r'latest',
        r'stable',
        r'beta',
        r'alpha',
        r'rc\d*',            # rc, rc1, rc2
        r'snapshot',
        r'release',
    ]
}

# Example real-world file names for training
TRAINING_EXAMPLES = [
    # Documents
    ("Q4_2023_Financial_Report_FINAL.pdf", "documents"),
    ("Project_Requirements_v2.1.docx", "documents"),
    ("Meeting_Minutes_2024-01-15.txt", "documents"),
    ("Research_Paper_Draft_v3.pdf", "documents"),
    
    # Spreadsheets
    ("Monthly_Budget_2024.xlsx", "spreadsheets"),
    ("Sales_Analytics_Q1.csv", "spreadsheets"),
    ("Expense_Tracker_2023.gsheet", "spreadsheets"),
    ("Project_Timeline_v2.xlsx", "spreadsheets"),
    
    # Code and Development
    ("UserAuthService.ts", "code"),
    ("data_processing_utils.py", "code"),
    ("ApiClient.java", "code"),
    ("docker-compose.yml", "config"),
    
    # Design
    ("Homepage_Redesign_v3.fig", "design"),
    ("Logo_Final_Export.ai", "design"),
    ("App_Wireframes_v2.sketch", "design"),
    
    # Machine Learning
    ("trained_model_v1.h5", "ml_models"),
    ("feature_extraction.ipynb", "code"),
    ("dataset_preprocessed.pkl", "ml_models"),
    
    # Mobile
    ("MyApp-release.apk", "mobile"),
    ("AppDelegate.swift", "code"),
    ("MainActivity.kt", "code"),
    
    # Project Management
    ("Project_Gantt_2024.gan", "project"),
    ("Sprint_Planning_Q1.trello", "project"),
    ("Release_Schedule_v2.mpp", "project"),
    
    # Modern Work Files
    ("zoom_meeting_recording_2024.mp4", "videos"),
    ("teams_chat_export.json", "data"),
    ("slack_workspace_backup.zip", "archives"),
    ("figma_design_export.fig", "design"),
    ("notion_workspace_export.md", "documents"),
    ("discord_server_backup.json", "data"),
    ("github_repository_archive.zip", "archives"),
    ("kubernetes_config.yaml", "config"),
    ("terraform_state.tf", "config"),
    ("jenkins_pipeline.groovy", "code"),
    
    # Creative Work
    ("youtube_thumbnail.psd", "design"),
    ("podcast_episode_01.mp3", "audio"),
    ("instagram_story.mp4", "videos"),
    ("tiktok_draft_final.mp4", "videos"),
    ("stream_overlay.png", "images"),
    
    # Common User Files
    ("Screenshot_2024-01-30.png", "images"),
    ("IMG_20240130_123456.jpg", "images"),
    ("VID_20240130_123456.mp4", "videos"),
    ("voice_note_01.m4a", "audio"),
    ("backup_2024-01-30.zip", "archives")
]

TRAINING_EXAMPLES.extend([
    # Modern Development
    ("docker-compose.prod.yml", "container"),
    ("kubernetes-deployment.yaml", "container"),
    ("terraform.tfstate", "container"),
    ("helm-values.yaml", "container"),
    ("Dockerfile.dev", "container"),
    
    # Modern Web Development
    ("next.config.js", "web"),
    ("tailwind.config.js", "web"),
    ("vite.config.ts", "web"),
    ("package-lock.json", "config"),
    ("yarn.lock", "config"),
    
    # Modern Design Tools
    ("design-system.figma", "design"),
    ("brand-guidelines.sketch", "design"),
    ("ui-components.xd", "design"),
    ("animation-prototype.aep", "design"),
    
    # Cloud Native
    ("eks-cluster.yaml", "container"),
    ("cloud-function.js", "code"),
    ("lambda-handler.py", "code"),
    ("gcp-config.json", "config"),
    
    # AI/ML
    ("transformer-model.pt", "ml_models"),
    ("dataset-prep.ipynb", "code"),
    ("model-metrics.csv", "data"),
    ("hyperparameters.yaml", "config"),
    ("embeddings.npy", "ml_models"),
    
    # Modern Collaboration
    ("confluence-export.pdf", "documents"),
    ("miro-board.pdf", "documents"),
    ("figma-components.json", "design"),
    ("notion-workspace.md", "documents"),
    
    # Game Development
    ("player-controller.cs", "code"),
    ("game-level.unity", "game"),
    ("character-model.fbx", "3d_models"),
    ("game-assets.unitypackage", "game"),
    
    # Mobile Development
    ("AppDelegate.swift", "mobile"),
    ("MainActivity.kt", "mobile"),
    ("app-release.aab", "mobile"),
    ("Podfile.lock", "config"),
    
    # Social Media Content
    ("instagram-story-template.psd", "design"),
    ("youtube-thumbnail.png", "images"),
    ("tiktok-video-edit.mp4", "videos"),
    ("podcast-episode.mp3", "audio"),
    
    # Modern Work
    ("remote-meeting-recording.mp4", "videos"),
    ("team-standup-notes.md", "documents"),
    ("sprint-retrospective.pdf", "documents"),
    ("product-roadmap-2024.xlsx", "spreadsheets"),
    
    # Security and DevOps
    ("ssl-certificate.pem", "security"),
    ("jenkins-pipeline.groovy", "code"),
    ("github-actions.yml", "config"),
    ("nginx.conf", "config"),
    
    # 3D and CAD
    ("product-design.step", "cad"),
    ("assembly-model.dwg", "cad"),
    ("3d-print.stl", "3d_models"),
    ("architectural-plan.dxf", "cad")
])