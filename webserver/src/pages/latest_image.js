import React, { useEffect, useState } from 'react';
import { fetchImageList } from '../utils/imageFetcher';

const latest_image = () => {
  const [images, setImages] = useState([]);

  useEffect(() => {
    fetchImageList()
      .then(data => {
        console.log("✅ 받아온 이미지들:", data);
        setImages(data);
      })
      .catch(err => {
        console.error("❌ 이미지 불러오기 실패:", err);
      });
  }, []);

  const formatDate = (ts) => {
    const date = new Date(ts);
    return date.toLocaleString('ko-KR');
  };

  return (
    <div className="p-6 max-w-screen-xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">전체 저장된 이미지 목록</h1>
      <div className="grid grid-cols-3 gap-6">
        {images.length === 0 ? (
          <div className="text-gray-500">불러올 이미지가 없습니다.</div>
        ) : (
          images.map((img, idx) => (
            <div key={idx} className="border p-2 text-center space-y-2">
              <div className="h-48 flex items-center justify-center border">
                <img
                  src={img.url}
                  alt={img.name}
                  className="max-h-full object-contain"
                  onError={() => console.log("❌ 로드 실패:", img.url)}
                />
              </div>
              <div className="text-sm text-gray-800 font-semibold">{img.name}</div>
              <div className="text-xs text-gray-500">{formatDate(img.timestamp)}</div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default latest_image;
