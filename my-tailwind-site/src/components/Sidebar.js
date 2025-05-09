// components/Sidebar.js
import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => (
  <div className="flex flex-col items-center py-8 space-y-4">
    <Link to="/latest-image">
      <button className="bg-black text-white py-3 px-4 rounded w-24 text-sm">최근 사진</button>
    </Link>
    <Link to="/latest-audio">
      <button className="bg-black text-white py-3 px-4 rounded w-24 text-sm">최근 음성</button>
    </Link>
  </div>
);

export default Sidebar;