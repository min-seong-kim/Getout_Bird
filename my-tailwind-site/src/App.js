import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import ImageSection from './components/ImageSection';
import StatusText from './components/StatusText';
import Footer from './components/Footer';

function App() {
  return (
    <div className="bg-white p-6 font-sans">
      <div className="max-w-screen-lg mx-auto border border-black">
        <Navbar />
        <div className="grid grid-cols-5 border-b border-black min-h-[300px]">
          <Sidebar />
          <ImageSection />
        </div>
        <StatusText />
        <Footer />
      </div>
    </div>
  );
}

export default App;

