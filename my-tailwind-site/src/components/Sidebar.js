// components/Sidebar.js
import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => (
  <div className="flex flex-col items-center py-8 space-y-16">
    <Link to="/latest-image">
      <button className="bg-black text-white py-4 px-6 rounded w-32 text-base font-semibold">
        최근 사진
      </button>
    </Link>
    <Link to="/latest-audio">
      <button className="bg-black text-white py-4 px-6 rounded w-32 text-base font-semibold">
        최근 음성
      </button>
    </Link>
  </div>
);


export default Sidebar;