// // Sample project data (in a real app, this would come from an API)
// const projects = {
//   1: {
//     name: 'App Explainer Video',
//     client: 'Tech Startup',
//     project_type: 'Explainer Video',
//     date: '2023-05-15',
//     description: `
//             <p>Client wanted a fun and simple way to explain their new app. We added character animation and upbeat music to keep it light while effectively communicating the app's value proposition.</p>
//             <p>The video was designed to be used on their landing page, in social media campaigns, and as part of their investor pitch materials. The playful animation style matched their brand personality while maintaining professionalism.</p>
//             <p>Since launching the video, the client reported a 40% increase in sign-ups and significantly higher engagement on their social media posts featuring the animation.</p>
//         `,
//     videoUrl: 'https://example.com/video1.mp4',
//     thumbnailUrl: 'https://via.placeholder.com/1200x675',
//     goals: [
//       'Explain app functionality in under 90 seconds',
//       'Increase user sign-ups',
//       'Create shareable content for social media',
//       'Establish brand personality',
//     ],
//     style: [
//       '2D character animation',
//       'Bright, playful color palette',
//       'Modern geometric elements',
//       'Smooth transitions between scenes',
//     ],
//     results: [
//       '40% increase in sign-ups',
//       '25% higher engagement on social media',
//       'Used in successful funding round',
//       'Client satisfaction: 5/5 stars',
//     ],
//     relatedProjects: [2, 3],
//   },
//   2: {
//     name: 'Online Course Intro',
//     client: 'Educational Platform',
//     project_type: 'Educational Video',
//     date: '2023-03-22',
//     description: `
//             <p>Created an engaging intro sequence for an online course that helped increase student engagement and completion rates. The animation simplified complex concepts through visual storytelling.</p>
//             <p>The client wanted to reduce their course dropout rate and make the material more accessible to visual learners. We developed a series of animated explanations that became the most rewatched portions of the course.</p>
//         `,
//     videoUrl: 'https://example.com/video2.mp4',
//     thumbnailUrl: 'https://via.placeholder.com/1200x675',
//     goals: [
//       'Simplify complex course material',
//       'Increase course completion rates',
//       'Create reusable educational assets',
//       'Enhance student engagement',
//     ],
//     style: [
//       'Whiteboard animation style',
//       'Clean, academic color scheme',
//       'Step-by-step visual explanations',
//       'Minimalist character designs',
//     ],
//     results: [
//       '28% increase in course completion',
//       '60% of students cited animations as most helpful',
//       'Now used across all their courses',
//       'Reduced support questions by 35%',
//     ],
//     relatedProjects: [1, 3],
//   },
//   3: {
//     name: 'Product Demo',
//     client: 'E-commerce Brand',
//     project_type: 'Explainer Video',
//     date: '2023-01-10',
//     description: `
//             <p>Animated product demo that highlighted key features and resulted in a 30% increase in conversions. The video showcased the product from multiple angles with dynamic transitions.</p>
//             <p>The client needed to demonstrate their physical product's features without expensive live-action filming. Our 3D animation provided a cost-effective solution that could be easily updated as the product evolved.</p>
//         `,
//     videoUrl: 'https://example.com/video3.mp4',
//     thumbnailUrl: 'https://via.placeholder.com/1200x675',
//     goals: [
//       'Showcase product features',
//       'Increase online conversions',
//       'Create versatile marketing asset',
//       'Highlight unique selling points',
//     ],
//     style: [
//       '3D product animation',
//       'Realistic materials and lighting',
//       'Dynamic camera movements',
//       'Clean technical callouts',
//     ],
//     results: [
//       '30% increase in conversions',
//       'Reduced product returns by 22%',
//       'Used in email campaigns and trade shows',
//       'Client renewed for 3 more videos',
//     ],
//     relatedProjects: [1, 2],
//   },
// }

// document.addEventListener('DOMContentLoaded', function () {
//   // Get project ID from URL
//   const urlParams = new URLSearchParams(window.location.search)
//   const projectId = urlParams.get('id')

//   // Load project data
//   if (projectId && projects[projectId]) {
//     loadProject(projects[projectId])
//   } else {
//     document.getElementById('project-content').innerHTML = `
//             <div class="error-message" style="text-align: center; padding: 2rem;">
//                 <span class="material-symbols-outlined" style="font-size: 3rem; color: var(--md-sys-color-error);">
//                     error
//                 </span>
//                 <h2>Project Not Found</h2>
//                 <p>The requested project could not be loaded.</p>
//                 <a href="portfolio.html" class="btn btn-primary">
//                     <span class="material-symbols-outlined">collections</span>
//                     Back to Portfolio
//                 </a>
//             </div>
//         `
//   }
// })

// function loadProject(project) {
//   const relatedProjectsHtml = project.relatedProjects
//     .map((id) => {
//       const related = projects[id]
//       return `
//             <a href="portfolio-detail.html?id=${id}" class="related-card">
//                 <div class="related-image">
//                     <img src="${related.thumbnailUrl}" alt="${related.name}">
//                 </div>
//                 <div class="related-content">
//                     <h4>${related.name}</h4>
//                     <div class="related-meta">${related.project_type}</div>
//                 </div>
//             </a>
//         `
//     })
//     .join('')

//   document.getElementById('project-content').innerHTML = `
//         <div class="project-header">
//             <h1>${project.name}</h1>
//             <div class="project-meta">
//                 <div class="meta-item">
//                     <span class="material-symbols-outlined">person</span>
//                     <span>Client: ${project.client}</span>
//                 </div>
//                 <div class="meta-item">
//                     <span class="material-symbols-outlined">category</span>
//                     <span>Type: ${project.project_type}</span>
//                 </div>
//                 <div class="meta-item">
//                     <span class="material-symbols-outlined">calendar_month</span>
//                     <span>Date: ${new Date(project.date).toLocaleDateString(
//                       'en-US',
//                       { year: 'numeric', month: 'long', day: 'numeric' }
//                     )}</span>
//                 </div>
//             </div>
//         </div>

//         <div class="video-container">
//             <video controls poster="${project.thumbnailUrl}">
//                 <source src="${project.videoUrl}" type="video/mp4">
//                 Your browser does not support the video tag.
//             </video>
//         </div>

//         <div class="project-description">
//             <h2>Project Overview</h2>
//             ${project.description}
//         </div>

//         <div class="project-details">
//             <div class="detail-card">
//                 <h3><span class="material-symbols-outlined">target</span>Goals</h3>
//                 <ul>
//                     ${project.goals.map((goal) => `<li>${goal}</li>`).join('')}
//                 </ul>
//             </div>

//             <div class="detail-card">
//                 <h3><span class="material-symbols-outlined">palette</span>Style</h3>
//                 <ul>
//                     ${project.style
//                       .map((style) => `<li>${style}</li>`)
//                       .join('')}
//                 </ul>
//             </div>

//             <div class="detail-card">
//                 <h3><span class="material-symbols-outlined">check_circle</span>Results</h3>
//                 <ul>
//                     ${project.results
//                       .map((result) => `<li>${result}</li>`)
//                       .join('')}
//                 </ul>
//             </div>
//         </div>

//         <div class="related-projects">
//             <h2>Related Projects</h2>
//             <p>Check out some of my other similar projects</p>

//             <div class="related-grid">
//                 ${relatedProjectsHtml}
//             </div>
//         </div>
//     `

//   // Update page title
//   document.title = `${project.name} - TopResource`
// }
