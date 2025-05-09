import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import ImageAudioSection from './components/ImageSection';
import StatusSection from './components/StatusText';
import Footer from './components/Footer';
import Latest_image from './pages/latest_image';
import Latest_audio from './pages/latest_audio';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100 font-sans flex flex-col justify-between">
        <Navbar />
        <main className="flex-grow">
          <Routes>
            <Route
              path="/"
              element={
                <div className="max-w-screen-xl mx-auto grid grid-cols-12 border border-black">
                  <div className="col-span-2 bg-white border-r border-black">
                    <Sidebar />
                  </div>
                  <div className="col-span-10 bg-white">
                    <ImageAudioSection />
                  </div>
                </div>
              }
            />
            <Route path="/latest-image" element={<Latest_image />} />
            <Route path="/latest-audio" element={<Latest_audio />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;