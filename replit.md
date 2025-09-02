# Flickbytes Landing Page

## Overview

Flickbytes is a short video threading application that allows users to create dynamic conversations through 10-second video clips. This repository contains a Flask-based web application that serves a professional, responsive landing page for the platform. The application features a dark modern theme with teal, blue, and gold accent gradients, designed to showcase the platform's innovative video threading capabilities and community-focused approach.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templating with Flask for server-side rendering
- **Styling Approach**: Inline CSS with CSS custom properties (CSS variables) for consistent theming
- **Responsive Design**: CSS Grid and Flexbox for mobile-first responsive layouts
- **Typography**: Google Fonts integration (Inter font family)
- **Icons**: Feather Icons library for consistent iconography
- **Interactive Elements**: CSS hover effects and transitions for enhanced user experience

### Backend Architecture
- **Web Framework**: Flask (Python) - lightweight WSGI web application framework
- **Session Management**: Flask's built-in session handling with configurable secret key
- **Environment Configuration**: Environment variable support for sensitive configuration (SESSION_SECRET)
- **Development Setup**: Debug mode enabled with configurable host and port binding
- **Application Structure**: Modular design with separate app.py and main.py entry points

### Design System
- **Color Scheme**: Dark theme with CSS custom properties for consistent color management
- **Gradient System**: Multiple gradient definitions for primary, secondary, and accent elements
- **Typography Scale**: Inter font family with multiple weights (300-800)
- **Spacing System**: Container-based layout with max-width constraints
- **Component Architecture**: Card-based components for features, benefits, and content sections

### Page Structure
- **Navigation**: Fixed header with logo and action buttons
- **Hero Section**: Split layout with headline, CTA buttons, and video placeholder
- **Feature Showcase**: Grid-based layout for platform capabilities
- **Admin Dashboard**: Dedicated section highlighting FireCMS-powered administration
- **Call-to-Action**: Centered conversion-focused section
- **Footer**: Simple branding and links

## External Dependencies

### Frontend Libraries
- **Google Fonts**: Inter font family for modern typography
- **Feather Icons**: SVG icon library for consistent UI elements

### Development Dependencies
- **Flask**: Python web framework for serving the application
- **Jinja2**: Template engine (included with Flask)

### Hosting Requirements
- **Python Runtime**: Compatible with Python web hosting platforms
- **Static File Serving**: CSS and JavaScript are inlined, minimal static file requirements
- **Environment Variables**: Support for SESSION_SECRET configuration

### Future Integration Points
- **Video Hosting**: Placeholder elements ready for video content integration
- **FireCMS**: Admin dashboard integration mentioned in content
- **Analytics**: Structure prepared for tracking and analytics implementation
- **Authentication**: Session management foundation in place for user authentication