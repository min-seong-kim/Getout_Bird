import React, { useEffect, useState } from 'react';
import { fetchImageList } from '../utils/imageFetcher';

const latest_image = () => {
  const [images, setImages] = useState([]);
  const [analyzedImages, setAnalyzedImages] = useState([]);

  useEffect(() => {
    fetchImageList()
      .then(data => {
        console.log("✅ 받아온 원본 이미지들:", data);
        setImages(data);
      })
      .catch(err => {
        console.error("❌ 원본 이미지 불러오기 실패:", err);
      });

    fetch('http://220.149.235.221:4000/api/images_result/')
      .then(res => res.json())
      .then(fileList => {
        const sorted = fileList
          .filter(name => name.endsWith('.jpg'))
          .sort((a, b) => {
            const getTime = f => {
              const match = f.match(/frame_(\d+)\.jpg/);
              return match ? parseInt(match[1]) : 0;
            };
            return getTime(b) - getTime(a);
          });

        const fullData = sorted.map(name => ({
          name,
          url: `http://220.149.235.221:4000/images_result/${name}`,
          timestamp: parseInt(name.match(/frame_(\d+)\.jpg/)?.[1] || 0)
        }));

        console.log("✅ 받아온 AI 분석 이미지들:", fullData);
        setAnalyzedImages(fullData);
      })
      .catch(err => {
        console.error("❌ 분석 이미지 불러오기 실패:", err);
      });
  }, []);

  const formatDate = (ts) => {
    const date = new Date(ts);
    return date.toLocaleString('ko-KR');
  };

  return (
    <div className="p-6 max-w-screen-xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">전체 저장된 이미지 목록</h1>

      {/* 원본 이미지 섹션 */}
      <h2 className="text-xl font-semibold mb-4">📷 원본 이미지</h2>
      <div className="grid grid-cols-3 gap-6 mb-12">
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

      {/* 분석 이미지 섹션 */}
      <h2 className="text-xl font-semibold mb-4">🧠 AI가 분석한 이미지</h2>
      <div className="grid grid-cols-3 gap-6">
        {analyzedImages.length === 0 ? (
          <div className="text-gray-500">불러올 분석 이미지가 없습니다.</div>
        ) : (
          analyzedImages.map((img, idx) => (
            <div key={idx} className="border p-2 text-center space-y-2">
              <div className="h-48 flex items-center justify-center border">
                <img
                  src={img.url}
                  alt={img.name}
                  className="max-h-full object-contain"
                  onError={() => console.log("❌ 분석 이미지 로딩 실패:", img.url)}
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