# 🌱 Land-CRAFT Onboarding Navigator

A simple navigator chatbot designed to help PhD students find resources that are usually internally kept.

Resources linked are Sharepoint-protected so that externals are not permitted to access them. If one wants to implement this solution, consider using limited access points too.

![Land-CRAFT Navigator](https://img.shields.io/badge/Status-Active-brightgreen) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

## 🎯 Overview

The Land-CRAFT Onboarding Navigator is an interactive web-based chatbot that helps new PhD students quickly find relevant resources, documentation, tools, and groups within Land-CRAFT team. Built as a single HTML file with embedded CSS and JavaScript, it's designed to be lightweight, fast, and easy to deploy.

## ✨ Features

### 🤖 **Intelligent Chat Interface**
- Modern, responsive chatbot UI with smooth animations
- Typing indicators and message bubbles for natural conversation flow
- Mobile-friendly design that works on all devices

### 🧠 **Smart Keyword Detection**
- Advanced natural language processing for user queries
- Automatic routing to relevant resources based on detected keywords
- Scoring system for handling multiple keyword matches
- Fallback responses for unrecognized queries

### 📚 **Resource Categories**
- **Tutorials & Guides**: Step-by-step learning materials and letterhead creation guides
- **Documentation**: Technical references for Land-CRAFT tools (Landscape_DNDC, etc.)
- **Samples**: Templates, PhD plans, HPC examples, and grant applications
- **Tools & Software**: GitHub, Microsoft tools, and other essential software
- **Groups to Join**: WhatsApp and Teams communities for collaboration
- **Courses**: Relevant academic courses and training materials

### 💬 **Dual Input Methods**
- **Button Navigation**: Click-through options for structured browsing
- **Text Input**: Type natural language queries like "How do I create letterheads?" or "I need documentation"

### 🎨 **Modern Design**
- Gradient backgrounds and smooth animations
- Customizable avatar system (emoji or custom images)
- Professional color scheme suitable for academic environments
- Responsive layout that adapts to screen size

## 🚀 Quick Start

### **Option 1: Direct Use**
1. Clone or download this repository
2. Open `index.html` in any modern web browser
3. Start chatting!

### **Option 2: GitHub Pages Deployment**
1. Fork this repository
2. Go to Settings → Pages in your GitHub repo
3. Select "Deploy from a branch" → `main` branch
4. Your chatbot will be live at `https://yourusername.github.io/landcraft_onboarding_chatbot/`

### **Option 3: Custom Hosting**
Upload the `index.html` file to any web hosting service (Netlify, Vercel, etc.)

## 🛠️ Customization

### **Adding New Resources**
Edit the `resources` object in the JavaScript section:

```javascript
const resources = {
    your_resource: {
        name: "Your Resource Name",
        url: "https://your-link-here.com",
        description: "Description of your resource",
        keywords: ["keyword1", "keyword2", "relevant", "terms"]
    }
};
```

### **Customizing the Avatar**
Replace the robot emoji with your preferred icon:

**Option 1: Emoji**
```javascript
// Find this line and replace 🤖 with your emoji
<div class="bot-avatar">🌱</div>
```

**Option 2: Custom Image**
1. Add your image to an `images/` folder
2. Update the CSS:
```css
.bot-avatar {
    background-image: url('images/your-avatar.png');
    background-size: 25px 25px;
    background-position: center;
    background-repeat: no-repeat;
}
```

### **Updating Keywords**
Enhance keyword detection by adding terms to the `keywords` arrays in each resource. The system automatically matches user input against these keywords.

### **Styling Customization**
All styles are contained within the `<style>` section. Key customizable elements:
- Color gradients
- Font families
- Button styles
- Animation timings
- Layout dimensions

## 📖 How It Works

### **Keyword Detection Algorithm**
1. User types a query (e.g., "I need help with tutorials")
2. System converts query to lowercase and searches for keyword matches
3. Each resource gets a score based on keyword frequency
4. Results are ranked and presented:
   - **Single match**: Direct link to resource
   - **Multiple matches**: Contextual options
   - **No matches**: All available resources

### **Resource Structure**
Each resource contains:
- **Name**: Display title
- **URL**: Link to the actual resource (SharePoint, etc.)
- **Description**: Brief explanation
- **Keywords**: Array of searchable terms

### **Conversation Flow**
```
Welcome Message → User Input → Keyword Analysis → Response Generation → Resource Links
```

## 🏗️ Technical Architecture

### **Built With**
- **HTML5**: Semantic structure and accessibility
- **CSS3**: Modern styling with flexbox and animations
- **Vanilla JavaScript**: No external dependencies
- **ES6+ Features**: Arrow functions, template literals, destructuring

### **Browser Support**
- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

### **Performance**
- **Load time**: < 1 second
- **Bundle size**: < 50KB
- **Responsive**: Works on all screen sizes
- **Accessible**: ARIA labels and keyboard navigation

## 📁 Project Structure

```
landcraft_onboarding_chatbot/
├── index.html          # Main application file
├── README.md          # This file
├── images/            # Custom avatars and assets (optional)
│   └── bot-avatar.png
└── .gitignore         # Git ignore file (optional)
```

## 🤝 Contributing

### **Adding New Features**
1. Fork the repository
2. Create a feature branch: `git checkout -b new-feature`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### **Reporting Issues**
- Use GitHub Issues to report bugs
- Include browser information and steps to reproduce
- Suggest improvements or new features

### **Development Guidelines**
- Keep all code in the single HTML file for portability
- Test on multiple browsers and devices
- Maintain accessibility standards
- Document any new configuration options

## 📚 Documentation

### **For End Users**
- Type natural language queries in the input field
- Use keywords like "tutorial", "documentation", "examples", etc.
- Click buttons for structured navigation
- All resources open in new tabs

### **For Administrators**
- Update SharePoint URLs in the `resources` object
- Add new keywords to improve search accuracy
- Customize styling in the CSS section
- Monitor usage through web analytics (if implemented)

## 🔧 Configuration

### **Required Setup**
1. Update SharePoint URLs in the `resources` object
2. Customize the welcome message and branding
3. Add institution-specific resources
4. Test all links and functionality

### **Optional Enhancements**
- Add Google Analytics tracking
- Implement usage statistics
- Add more sophisticated NLP
- Create admin panel for resource management

## 📊 Analytics & Monitoring

### **Recommended Tracking**
- Page views and session duration
- Most searched keywords
- Resource click-through rates
- User journey analysis

### **Implementation Example**
```html
<!-- Add to <head> section -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋‍♀️ Support

### **For Technical Issues**
- Check browser console for JavaScript errors
- Ensure all SharePoint links are accessible
- Verify internet connection for external resources

### **For Content Updates**
- Contact the repository owner
- Submit pull requests for resource additions
- Report broken or outdated links

### **Contact Information**
- **Team**: Land-CRAFT at Aarhus University
- **Repository**: [github.com/GraceBarbacias/landcraft_onboarding_chatbot](https://github.com/GraceBarbacias/landcraft_onboarding_chatbot)

---

## 🌟 Acknowledgments

Built for the Land-CRAFT team at Aarhus University to streamline PhD student onboarding and resource discovery.

**Warm welcome! 🔬🌱**
