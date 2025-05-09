import { Link } from 'react-router-dom';

const Navbar = () => (
  <nav className="w-full bg-white shadow-md p-4">
    <div className="max-w-screen-xl mx-auto flex items-center justify-between">
      {/* 홈으로 이동하는 로고 or 제목 */}
      <Link to="/" className="text-2xl font-bold text-blue-600 hover:underline">
        AI 새 쫓기 시스템
      </Link>
    </div>
  </nav>
);

export default Navbar;