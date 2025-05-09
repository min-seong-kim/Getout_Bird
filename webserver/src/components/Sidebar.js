// components/Sidebar.js
import React from 'react';

const Sidebar = () => (
  <div className="flex flex-col items-center py-8 space-y-4">
    <button className="bg-black text-white py-2 px-4 rounded w-24 text-sm">최근 사진</button>
    <button className="bg-black text-white py-2 px-4 rounded w-24 text-sm">최근 음성</button>
  </div>
);

export default Sidebar;