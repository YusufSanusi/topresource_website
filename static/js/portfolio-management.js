// Sample portfolio data (in a real app, this would come from a database)
// let portfolioData = [
//   {
//     id: 1,
//     title: 'App Explainer Video',
//     client: 'Tech Startup',
//     projectType: 'Explainer Video',
//     projectDate: '2023-05-15',
//     description:
//       'Client wanted a fun and simple way to explain their new app. We added character animation and upbeat music to keep it light.',
//     videoUrl: 'https://example.com/video1.mp4',
//     thumbnailUrl: 'https://via.placeholder.com/400x225',
//   },
//   {
//     id: 2,
//     title: 'Online Course Intro',
//     client: 'Educational Platform',
//     projectType: 'Educational Video',
//     projectDate: '2023-03-22',
//     description:
//       'Created an engaging intro sequence for an online course that helped increase student engagement and completion rates.',
//     videoUrl: 'https://example.com/video2.mp4',
//     thumbnailUrl: 'https://via.placeholder.com/400x225',
//   },
//   {
//     id: 3,
//     title: 'Product Demo',
//     client: 'E-commerce Brand',
//     projectType: 'Explainer Video',
//     projectDate: '2023-01-10',
//     description:
//       'Animated product demo that highlighted key features and resulted in a 30% increase in conversions.',
//     videoUrl: 'https://example.com/video3.mp4',
//     thumbnailUrl: 'https://via.placeholder.com/400x225',
//   },
// ]

// DOM Elements
const addNewBtn = document.getElementById('addNewBtn')
const addPortfolioForm = document.getElementById('addPortfolioForm')
const portfolioForm = document.getElementById('portfolioForm')
const cancelBtn = document.getElementById('cancelBtn')
const portfolioItems = document.getElementById('portfolioItems')
// const deleteModal = document.getElementById('deleteModal')
const closeModal = document.getElementById('closeModal')
// const cancelDelete = document.getElementById('cancelDelete')
// const confirmDelete = document.getElementById('confirmDelete')

// Form elements
// const projectId = document.getElementById('id')
const title = document.getElementById('title')
const client = document.getElementById('client')
const projectType = document.getElementById('project_type')
const projectDate = document.getElementById('date')
const description = document.getElementById('description')
const featuredVideo = document.getElementById('featured_video')
const videoUpload = document.getElementById('videoUpload')
const videoPreview = document.getElementById('videoPreview')
const videoPlayer = document.getElementById('videoPlayer')
const videoFileName = document.getElementById('videoFileName')
const removeVideo = document.getElementById('removeVideo')
// const thumbnailImage = document.getElementById('thumbnailImage')
// const thumbnailFileName = document.getElementById('thumbnailFileName')

// State variables
// let currentProjectId = null
// let projectToDelete = null

// Initialize the page
document.addEventListener('DOMContentLoaded', function () {
  // Event listeners
  addNewBtn.addEventListener('click', showAddForm)
  cancelBtn.addEventListener('click', resetForm)

  // File upload handlers
  videoUpload.addEventListener('click', () => featuredVideo.click())
  featuredVideo.addEventListener('change', handleVideoUpload)
  removeVideo.addEventListener('click', removeUploadedVideo)

  // Modal handlers
  // closeModal.addEventListener(
  //   'click',
  //   () => (deleteModal.style.display = 'none')
  // )
  // cancelDelete.addEventListener(
  //   'click',
  //   () => (deleteModal.style.display = 'none')
  // )
  // confirmDelete.addEventListener('click', deleteProject)

  // Close modal when clicking outside
  // deleteModal.addEventListener('click', function (e) {
  //   if (e.target === deleteModal) {
  //     deleteModal.style.display = 'none'
  //   }
  // })
})

// // Render portfolio items
// function renderPortfolioItems() {
//   portfolioItems.innerHTML = ''

//   if (portfolioData.length === 0) {
//     portfolioItems.innerHTML =
//       '<p>No portfolio items yet. Click "Add New Project" to get started.</p>'
//     return
//   }

//   portfolioData.forEach((project) => {
//     const projectElement = document.createElement('div')
//     projectElement.className = 'portfolio-item'
//     projectElement.innerHTML = `
//             <div class="portfolio-item-image">
//                 <img src="${project.thumbnailUrl}" alt="${project.name}">
//                 <div class="portfolio-item-actions">
//                     <button class="action-btn edit" data-id="${project.id}">
//                         <span class="material-symbols-outlined">edit</span>
//                     </button>
//                     <button class="action-btn delete" data-id="${project.id}">
//                         <span class="material-symbols-outlined">delete</span>
//                     </button>
//                 </div>
//             </div>
//             <div class="portfolio-item-content">
//                 <h3>${project.title}</h3>
//                 <p><strong>Client:</strong> ${project.client}</p>
//                 <p><strong>Type:</strong> ${project.project_type}</p>
//                 <p><strong>Date:</strong> ${formatDate(
//       project.date
//     )}</p>
//             </div>
//         `

//     portfolioItems.appendChild(projectElement)
//   })

//   // // Add event listeners to action buttons
//   // document.querySelectorAll('.action-btn.edit').forEach((btn) => {
//   //   btn.addEventListener('click', (e) => {
//   //     const id = parseInt(btn.getAttribute('data-id'))
//   //     editProject(id)
//   //     e.stopPropagation()
//   //   })
//   // })

//   // document.querySelectorAll('.action-btn.delete').forEach((btn) => {
//   //   btn.addEventListener('click', (e) => {
//   //     const id = parseInt(btn.getAttribute('data-id'))
//   //     showDeleteModal(id)
//   //     e.stopPropagation()
//   //   })
//   // })
// }

// Show add form
function showAddForm() {
  resetForm()
  addPortfolioForm.style.display = 'block'
  addNewBtn.style.display = 'none'
  window.scrollTo({ top: addPortfolioForm.offsetTop - 20, behavior: 'smooth' })
}

// Reset form
function resetForm() {
  portfolioForm.reset()
  // currentProjectId = null
  // projectId.value = ''
  videoPreview.style.display = 'none'
  videoPlayer.style.display = 'none'
  addPortfolioForm.style.display = 'none'
  addNewBtn.style.display = 'flex'
}

// Handle form submission
// function handleFormSubmit(e) {
//   e.preventDefault()

//   const project = {
//     name: title.value,
//     client: client.value,
//     project_type: projectType.value,
//     date: projectDate.value,
//     description: description.value,
//     // In a real app, you would upload files to a server and get URLs
//     videoUrl: featuredVideo.files[0]
//       ? URL.createObjectURL(featuredVideo.files[0])
//       : '',
//     thumbnailUrl: projectThumbnail.files[0]
//       ? URL.createObjectURL(projectThumbnail.files[0])
//       : '',
//   }

//   if (currentProjectId) {
//     // Update existing project
//     const index = portfolioData.findIndex((p) => p.id === currentProjectId)
//     if (index !== -1) {
//       portfolioData[index] = { ...portfolioData[index], ...project }
//     }
//   } else {
//     // Add new project
//     const newId =
//       portfolioData.length > 0
//         ? Math.max(...portfolioData.map((p) => p.id)) + 1
//         : 1
//     portfolioData.push({ id: newId, ...project })
//   }

//   renderPortfolioItems()
//   resetForm()

//   // Show success message
//   alert('Project saved successfully!')
// }

// // Edit project
// function editProject(id) {
//   const project = portfolioData.find((p) => p.id === id)
//   if (!project) return

//   currentProjectId = id
//   projectId.value = id
//   title.value = project.name
//   client.value = project.client
//   projectType.value = project.project_type
//   projectDate.value = project.date
//   description.value = project.description

//   // Show form
//   addPortfolioForm.style.display = 'block'
//   addNewBtn.style.display = 'none'
//   window.scrollTo({ top: addPortfolioForm.offsetTop - 20, behavior: 'smooth' })
// }

// // Show delete confirmation modal
// function showDeleteModal(id) {
//   projectToDelete = id
//   deleteModal.style.display = 'flex'
// }

// // Delete project
// function deleteProject() {
//   portfolioData = portfolioData.filter((p) => p.id !== projectToDelete)
//   // renderPortfolioItems()
//   deleteModal.style.display = 'none'
//   projectToDelete = null
// }

// Handle video upload
function handleVideoUpload(e) {
  const file = e.target.files[0]
  if (!file) return

  if (!file.type.match('video.*')) {
    alert('Please select a video file')
    return
  }

  if (file.size > 50 * 1024 * 1024) {
    // 50MB
    alert('Video file is too large (max 50MB)')
    return
  }

  videoPreview.style.display = 'block'
  videoPlayer.style.display = 'block'
  videoPlayer.src = URL.createObjectURL(file)
  videoFileName.querySelector('.selected-file-name').textContent = file.name
}

// Remove uploaded video
function removeUploadedVideo() {
  featuredVideo.value = ''
  videoPreview.style.display = 'none'
  videoPlayer.style.display = 'none'
  videoPlayer.src = ''
}

// Handle thumbnail upload
// function handleThumbnailUpload(e) {
//   const file = e.target.files[0]
//   if (!file) return

//   if (!file.type.match('image.*')) {
//     alert('Please select an image file')
//     return
//   }

//   if (file.size > 5 * 1024 * 1024) {
//     // 5MB
//     alert('Image file is too large (max 5MB)')
//     return
//   }

//   thumbnailPreview.style.display = 'block'
//   thumbnailImage.style.display = 'block'
//   thumbnailImage.src = URL.createObjectURL(file)
//   thumbnailFileName.querySelector('.selected-file-name').textContent = file.name
// }

// Remove uploaded thumbnail
// function removeUploadedThumbnail() {
//   projectThumbnail.value = ''
//   thumbnailPreview.style.display = 'none'
//   thumbnailImage.style.display = 'none'
//   thumbnailImage.src = ''
// }

// Format date for display
function formatDate(dateString) {
  const options = { year: 'numeric', month: 'long', day: 'numeric' }
  return new Date(dateString).toLocaleDateString(undefined, options)
}
