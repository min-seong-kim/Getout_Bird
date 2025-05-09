// App.js
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import ImageAudioSection from './components/ImageSection';
import StatusSection from './components/StatusText';
import Footer from './components/Footer';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 font-sans">
      <Navbar />
      <div className="max-w-screen-xl mx-auto grid grid-cols-12 border border-black">
        <div className="col-span-2 bg-white border-r border-black">
          <Sidebar />
        </div>
        <div className="col-span-10 bg-white">
          <ImageAudioSection />
        </div>
      </div>
      <StatusSection />
      <Footer />
    </div>
  );
}

export default App;